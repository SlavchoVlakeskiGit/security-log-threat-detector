import streamlit as st
import pandas as pd

from src.log_parser import parse_log_line
from src.rule_engine import detect_bruteforce, detect_off_hours_login
from src.alerts import export_alerts_csv, log_alerts

# Layout
st.set_page_config(page_title="Security Log Threat Detector", layout="wide")
st.title("Security Log Threat Detector")
st.write("Upload a log file and analyze suspicious activity in your network.")

#Sidebar
st.sidebar.header("Detection Settings")

threshold = st.sidebar.slider("Brute force threshold (failed logins)", 2, 10, 3)
window_minutes = st.sidebar.slider("Time window for brute force (minutes)", 1, 30, 5)

off_hours_start = st.sidebar.time_input("Off-hours start", value=pd.to_datetime("22:00").time())
off_hours_end = st.sidebar.time_input("Off-hours end", value=pd.to_datetime("06:00").time())

# File uploader
uploaded_file = st.file_uploader("Upload a log file", type=["txt", "log"])

# Only run if a file is uploaded
if uploaded_file is not None:
    # Read the uploaded file
    logs = uploaded_file.read().decode("utf-8").splitlines()

    # Parse log lines
    events = []
    for line in logs:
        parsed = parse_log_line(line.strip())
        if parsed:
            events.append(parsed)

    st.success(f"Loaded {len(events)} log entries")

    # Run detection rules
    alerts = []
    alerts.extend(detect_bruteforce(events, threshold=threshold, window_minutes=window_minutes))
    alerts.extend(detect_off_hours_login(events, start_hour=off_hours_start.hour, end_hour=off_hours_end.hour))

    # Display alerts
    if alerts:
        df = pd.DataFrame(alerts)
        st.subheader("Detected Threats")
        st.dataframe(df, use_container_width=True)

        # Export CSV and logs
        export_alerts_csv(alerts)
        log_alerts(alerts)

        st.success("Alerts exported to logs/alerts.csv and logs/security_alerts.log")
    else:
        st.info("No threats detected")