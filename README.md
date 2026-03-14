# Security Log Threat Detector

A Python-based security analysis tool that detects suspicious activity from authentication logs.

This project simulates a simplified **Security Information and Event Management (SIEM)** detection pipeline used by SOC analysts.

## Features

* Brute force login detection
* Time-window attack detection
* Off-hours login monitoring
* Alert pipeline with CSV export
* Security alert logging
* Modular detection engine
* Unit tests

## Project Structure

```
security-log-threat-detector
│
├── src
│   ├── main.py
│   ├── log_parser.py
│   ├── rule_engine.py
│   └── alerts.py
│
├── data
│   └── sample_logs.txt
│
├── logs
│   ├── alerts.csv
│   └── security_alerts.log
│
├── tests
│   └── test_rules.py
│
└── README.md
```

## Example Log Format

```
2026-03-12 08:15:23 FAILED_LOGIN user=alice ip=192.168.1.10
2026-03-12 23:30:10 LOGIN_SUCCESS user=alice ip=192.168.1.10
```

## Detection Rules

### Brute Force Detection

Flags users with multiple failed logins within a short time window.

### Off-Hours Login Detection

Detects successful logins occurring outside normal working hours.

## Running the Tool

Run the detection engine:

```
python -m src.main
```

Example output:

```
Security Alerts:

ALERT TYPE: BRUTE_FORCE_TIME_WINDOW
User: alice
IP: 192.168.1.10
```

Alerts will also be exported to:

```
logs/alerts.csv
logs/security_alerts.log
```

## Running Tests

```
python -m unittest discover tests
```

## Skills Demonstrated

* Python development
* Security log analysis
* Detection rule engineering
* SIEM-style alert pipelines
* Modular software architecture
* Unit testing

## Future Improvements

* Add IP reputation checks
* Add geolocation anomaly detection
* Support JSON log formats
* Add real-time log streaming
