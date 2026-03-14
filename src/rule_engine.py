from collections import defaultdict
from datetime import datetime

def detect_bruteforce(events, threshold=3, window_minutes=5):

    failures = defaultdict(list)
    alerts = []

    for event in events:

        if event["event"] == "FAILED_LOGIN":

            timestamp = datetime.strptime(event["timestamp"], "%Y-%m-%d %H:%M:%S")

            failures[event["user"]].append({
                "time": timestamp,
                "ip": event["ip"]
            })

    for user, attempts in failures.items():

        attempts.sort(key=lambda x: x["time"])

        for i in range(len(attempts) - threshold + 1):

            start = attempts[i]["time"]
            end = attempts[i + threshold - 1]["time"]

            if (end - start).seconds <= window_minutes * 60:

                alerts.append({
                    "type": "BRUTE_FORCE_TIME_WINDOW",
                    "user": user,
                    "ip": attempts[i]["ip"],
                    "attempts": threshold
                })

                break

    return alerts