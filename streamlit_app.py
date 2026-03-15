import streamlit as st
import pandas as pd

from src.log_parser import parse_log_line
from src.rule_engine import detect_bruteforce, detect_off_hours_login
from src.alerts import export_alerts_csv, log_alerts


# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="Security Log Threat Detector",
    layout="wide"
)

st.title("Security Log Threat Detector")
st.write("Analyze authentication logs and detect suspicious activity.")


# ------------------------------------------------
# SIDEBAR SETTINGS
# ------------------------------------------------

st.sidebar.header("Detection Settings")

threshold = st.sidebar.slider(
    "Brute Force Threshold",
    min_value=2,
    max_value=10,
    value=3,
    help="Number of failed login attempts required to trigger detection"
)

window_minutes = st.sidebar.slider(
    "Time Window (minutes)",
    min_value=1,
    max_value=30,
    value=5,
    help="Time window for brute force detection"
)

off_hours_start = st.sidebar.slider(
    "Off-hours start",
    0,
    23,
    22
)

off_hours_end = st.sidebar.slider(
    "Off-hours end",
    0,
    23,
    6
)


# ------------------------------------------------
# FILE UPLOAD
# ------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload a log file",
    type=["txt", "log"]
)


# ------------------------------------------------
# PROCESS LOG FILE
# ------------------------------------------------

if uploaded_file is not None:

    logs = uploaded_file.read().decode("utf-8").splitlines()

    events = []

    for line in logs:

        parsed = parse_log_line(line.strip())

        if parsed:
            events.append(parsed)

    st.success(f"Loaded {len(events)} log entries")


    # ------------------------------------------------
    # RUN DETECTION RULES
    # ------------------------------------------------

    alerts = []

    alerts.extend(
        detect_bruteforce(
            events,
            threshold=threshold,
            window_minutes=window_minutes
        )
    )

    alerts.extend(
        detect_off_hours_login(
            events,
            start_hour=off_hours_start,
            end_hour=off_hours_end
        )
    )


    # ------------------------------------------------
    # DISPLAY RESULTS
    # ------------------------------------------------

    if alerts:

        df = pd.DataFrame(alerts)

        st.subheader("Detected Threats")

        st.dataframe(
            df,
            use_container_width=True
        )


        # ------------------------------------------------
        # METRICS
        # ------------------------------------------------

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Total Alerts", len(df))

        with col2:
            st.metric("Unique Users Flagged", df["user"].nunique())


        # ------------------------------------------------
        # CHART
        # ------------------------------------------------

        st.subheader("Alerts by User")

        user_counts = df["user"].value_counts()

        st.bar_chart(user_counts)


        # ------------------------------------------------
        # DOWNLOAD CSV
        # ------------------------------------------------

        csv = df.to_csv(index=False)

        st.download_button(
            label="Download Alerts CSV",
            data=csv,
            file_name="alerts.csv",
            mime="text/csv"
        )


        # ------------------------------------------------
        # EXPORT ALERTS
        # ------------------------------------------------

        export_alerts_csv(alerts)
        log_alerts(alerts)

        st.success("Alerts exported to logs/alerts.csv and logs/security_alerts.log")

    else:

        st.info("No threats detected")