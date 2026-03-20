# Security Log Threat Detector

A Python project that parses authentication logs and flags suspicious patterns such as repeated failed logins and off-hours access.

I wanted one project that was a bit closer to security operations work, even if the detection logic stays simple.

## What it does

- reads sample authentication logs
- parses events into a structured format
- applies simple detection rules
- generates alerts for suspicious activity
- shows results in a lightweight Streamlit dashboard

## Detection rules in this version

The current project focuses on a small set of readable rules:

- repeated failed login attempts
- successful logins outside normal hours
- simple alert generation from matching events

That scope is intentional. I wanted the rules to stay understandable instead of turning this into a fake SIEM project.

## Tech stack

- Python
- Streamlit
- custom log parsing in Python
- basic tests

## Why I built it

The useful part here was the full flow:
1. ingest log data
2. parse it
3. apply rules
4. surface alerts in a readable way

I also liked that it forced me to think about how much detection logic is enough for a small project before it starts feeling inflated.

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

```bash
git clone https://github.com/SlavchoVlakeskiGit/security-log-threat-detector.git
cd security-log-threat-detector
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Notes

The detection is rule-based and intentionally simple. I preferred that because it keeps the project easier to follow and easier to talk through in an interview.

## Possible next improvements

- support more event types
- add severity levels
- improve rule configuration
- export flagged events

I initially tried adding more complex rules, but it made the project harder to follow, so I scaled it back.
