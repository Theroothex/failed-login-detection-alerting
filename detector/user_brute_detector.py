from collections import Counter

def detect_user_bruteforce(events, threshold=3):
    user_counter = Counter()

    for event in events:
        user = event["username"].strip()
        if user and user != "N/A" and user != "-":
            user_counter[user] += 1

    alerts = []

    for user, count in user_counter.items():
        if count >= threshold:
            alerts.append({
                "user": user,
                "attempts": count,
                "severity": "High"
            })

    return alerts
