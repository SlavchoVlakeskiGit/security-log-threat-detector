# Security Log Threat Detector

A Python project that parses authentication logs and flags simple suspicious patterns such as repeated failed logins and off-hours access.

I built it to practice log parsing, rule-based detection, and presenting results in a lightweight dashboard instead of just printing everything to the terminal.

## What it does

- reads sample authentication logs
- parses events into a structured format
- applies simple detection rules
- generates alerts for suspicious activity
- shows results in a small Streamlit dashboard

## Detection rules in this version

The current project focuses on a small set of understandable rules:

- repeated failed login attempts
- successful logins outside normal hours
- simple alert generation from matching events

That scope is intentional. It is a small detection project, not a full SIEM or SOC platform.

## Tech stack

- Python
- Streamlit
- log parsing with custom Python code
- basic tests

## Why I built it

I wanted one project in the portfolio that was closer to security operations work, but still simple enough to explain quickly.

The useful part here is not the size of the project. It is the flow:

1. ingest log data
2. parse it
3. apply rules
4. surface alerts in a readable way

## Project structure

```text
security-log-threat-detector/
├── data/
├── docs/
├── logs/
├── rules/
├── src/
├── tests/
├── streamlit_app.py
├── requirements.txt
└── README.md
```

## Run locally

### 1. Clone the repo

```bash
git clone https://github.com/SlavchoVlakeskiGit/security-log-threat-detector.git
cd security-log-threat-detector
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the dashboard

```bash
streamlit run streamlit_app.py
```

## Example log format

```text
2026-03-10 10:01:21 user=john ip=192.168.1.5 status=failure
2026-03-10 10:01:40 user=john ip=192.168.1.5 status=failure
2026-03-10 10:02:02 user=john ip=192.168.1.5 status=failure
2026-03-10 23:30:15 user=admin ip=10.0.0.8 status=success
```

## What this project shows

For a recruiter or hiring manager, this repo is mainly useful as evidence of:

- basic parsing and data processing
- translating simple security rules into code
- structuring a small Python project beyond a single script
- adding a minimal interface on top of raw analysis

## Next improvements

If I kept working on it, the most useful next steps would be:

- configurable rule thresholds
- better test coverage for parsing edge cases
- support for more than one input log format
- export of alerts to CSV or JSON

## Notes

Keep the README practical. This project should read like a small hands-on security coding exercise, not like an enterprise detection platform.
