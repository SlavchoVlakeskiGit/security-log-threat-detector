from src.log_parser import parse_log_line
from src.rule_engine import detect_bruteforce, detect_off_hours_login
from src.alerts import print_alerts


def load_logs(file_path):

    events = []

    with open(file_path) as f:

        for line in f:

            parsed = parse_log_line(line.strip())

            if parsed:
                events.append(parsed)

    return events


def main():

    logfile = "data/sample_logs.txt"

    events = load_logs(logfile)

    alerts = []   # <-- THIS WAS MISSING

    alerts.extend(detect_bruteforce(events))
    alerts.extend(detect_off_hours_login(events))

    print_alerts(alerts)


if __name__ == "__main__":
    main()