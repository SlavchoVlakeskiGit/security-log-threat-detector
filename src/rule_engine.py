from collections import defaultdict

def detect_bruteforce(events, threshold=3):

    failures = defaultdict(int)

    alerts = []

    for event in events:

        if event["event"] == "FAILED_LOGIN":

            failures[event["user"]] += 1

            if failures[event["user"]] >= threshold:

                alerts.append({
                    "type": "BRUTE_FORCE",
                    "user": event["user"],
                    "ip": event["ip"]
                })

    return alerts