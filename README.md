## Project Focus

This project focuses on detection logic and anomaly identification rather than API development or system architecture.

Unlike the log analytics API, this tool emphasizes detection logic and visualization rather than backend architecture.

# Security Log Threat Detector

A Python security log analysis tool that detects suspicious login activity from raw log files and presents findings in a simple Streamlit dashboard.

This project focuses on practical log parsing, failed login detection, alert generation, and lightweight security visualization.

## Features

- Parse authentication-style log entries from a text file
- Detect repeated failed login attempts by user and IP
- Flag suspicious patterns based on configurable thresholds
- Display findings in a Streamlit dashboard
- Show summary metrics and charts
- Export suspicious activity to CSV
- Includes sample log data for quick testing

## Tech Stack

- **Language:** Python
- **Interface:** Streamlit
- **Data Processing:** Pandas
- **Visualization:** Matplotlib / Streamlit charts
- **Export:** CSV

## Project Structure

```text
security-log-threat-detector/
│
├── data/
│   ├── sample_log.txt
│   └── suspicious_users.csv
├── screenshots/
│   └── dashboard.png
├── src/
│   ├── detector.py
│   ├── parser.py
│   └── utils.py
├── streamlit_app.py
├── requirements.txt
└── README.md
```

## What It Does

The application reads login-style log data and looks for suspicious patterns such as repeated failed login attempts from the same account or IP address.

It is intended as a lightweight security monitoring demo rather than a full SIEM or enterprise detection platform.

## Example Log Format

```text
2026-03-10 10:01:21 user=john ip=192.168.1.5 status=failure
2026-03-10 10:01:40 user=john ip=192.168.1.5 status=failure
2026-03-10 10:02:02 user=john ip=192.168.1.5 status=failure
2026-03-10 23:30:15 user=admin ip=10.0.0.8 status=success
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/SlavchoVlakeskiGit/security-log-threat-detector.git
cd security-log-threat-detector
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the dashboard

```bash
streamlit run streamlit_app.py
```

## Dashboard Preview

![Dashboard](docs/dashboard.png)

## Skills Demonstrated

- Python scripting
- Log parsing
- Basic threat detection logic
- Security-oriented data analysis
- Dashboard development with Streamlit
- CSV export workflow

## Limitations

- Detection logic is rule-based and intentionally lightweight
- Input format expects a consistent log pattern
- Designed for demo and portfolio use, not production deployment

## Future Improvements

- Add severity scoring for suspicious events
- Support multiple log formats
- Add IP reputation enrichment
- Add date-range filtering in the dashboard
- Add email or webhook alerts
- Package the tool as a standalone executable

## Why I Built This

I built this project to practice practical log analysis and security-focused detection logic in a way that feels more applied than a simple parser script.

## Author

**Slavcho Vlakeski**
