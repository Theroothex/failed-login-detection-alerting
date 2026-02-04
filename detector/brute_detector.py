from collections import Counter

def calculate_severity(count):
    if count <= 2:
        return "Low"
    else:
        return "High"   # 3+ = brute force


def detect_bruteforce(events, threshold=3):
    ip_counter = Counter()

    for event in events:
        ip = event["ip"].strip()
        if ip and ip != "N/A":
            ip_counter[ip] += 1

    alerts = []

    for ip, count in ip_counter.items():
        if count >= threshold:
            alerts.append({
                "ip": ip,
                "attempts": count,
                "severity": calculate_severity(count)
            })

    return alerts
