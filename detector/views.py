from django.shortcuts import render
from .log_reader import read_failed_logins
from .brute_detector import detect_bruteforce
from .models import FailedLoginEvent, BruteForceAlert


def dashboard(request):
    total_events = FailedLoginEvent.objects.count()
    total_alerts = BruteForceAlert.objects.count()

    return render(request, "dashboard.html", {
        "total_events": total_events,
        "total_alerts": total_alerts
    })


def events(request):
    logs = read_failed_logins(time_window_minutes=10)

    # Save failed login events
    for log in logs:
        FailedLoginEvent.objects.get_or_create(
            time=log["time"],
            ip_address=log["ip"],
            defaults={
                "username": log.get("username", ""),
                "logon_type": log.get("logon_type", "")
            }
        )

    ip_alerts = detect_bruteforce(logs, threshold=3)

    for alert in ip_alerts:
        existing = BruteForceAlert.objects.filter(
            ip_address=alert["ip"]
        ).order_by("-detected_at").first()

        if not existing or alert["attempts"] > existing.attempts:
            BruteForceAlert.objects.create(
                ip_address=alert["ip"],
                attempts=alert["attempts"],
                severity=alert["severity"]
            )

    return render(request, "events.html", {
        "logs": logs,
        "alerts": ip_alerts
    })


def alerts(request):
    alerts = BruteForceAlert.objects.order_by("-detected_at")
    return render(request, "alerts.html", {
        "alerts": alerts
    })
