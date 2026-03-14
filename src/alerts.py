import csv
import os


def print_alerts(alerts):

    if not alerts:
        print("No threats detected.")
        return

    print("\nSecurity Alerts:")

    for alert in alerts:
        print("ALERT TYPE:", alert.get("type"))
        print("User:", alert.get("user"))
        print("IP:", alert.get("ip"))
        print("-" * 30)


def export_alerts_csv(alerts):

    os.makedirs("logs", exist_ok=True)

    with open("logs/alerts.csv", "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow(["type", "user", "ip"])

        for alert in alerts:
            writer.writerow([
                alert.get("type"),
                alert.get("user"),
                alert.get("ip")
            ])


def log_alerts(alerts):

    os.makedirs("logs", exist_ok=True)

    with open("logs/security_alerts.log", "w") as f:

        for alert in alerts:
            f.write(
                f"{alert.get('type')} | user={alert.get('user')} | ip={alert.get('ip')}\n"
            )