# logwatch-lite

logwatch-lite is a lightweight Python tool focused on analyzing Linux
authentication logs to identify basic patterns that may indicate
suspicious login activity.

This project is designed to strengthen practical log analysis skills by
working directly with real authentication data. It emphasizes understanding
normal versus abnormal behavior, such as repeated failed logins, unusual
access timing, or unexpected user activity.

The goal is not to replace a full SIEM or enterprise monitoring solution,
but to build foundational defensive intuition, reinforce clean Python
project structure, and practice interpreting security-relevant logs in a
controlled learning context.

## Limitations and Assumptions

This tool is intentionally simple and designed for learning purposes. It does
not correlate events across multiple hosts, detect slow or distributed
brute-force attempts, or account for environmental context such as known
administrator IP addresses. Results should be interpreted as indicators for
further investigation, not definitive evidence of malicious activity.


