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

## Usage

This tool is intended to be run against a local Linux authentication log
(such as `/var/log/auth.log`) in a controlled learning environment.

Example:

```bash
python logwatch_lite.py /var/log/auth.log



