def print_alerts(alerts):

    if not alerts:
        print("No threats detected.")
        return

    print("\nSecurity Alerts:")

    for alert in alerts:

        print(f"""
ALERT TYPE: {alert['type']}
User: {alert['user']}
IP: {alert['ip']}
""")