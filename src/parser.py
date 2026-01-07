import re
from datetime import datetime

LOG_PATTERN = re.compile(
    r'(?P<month>\w+)\s+(?P<day>\d+)\s+(?P<time>\d+:\d+:\d+).*Failed password for (?P<user>\w+) from (?P<ip>\d+\.\d+\.\d+\.\d+)'
)

def parse_failed_logins(log_lines):
    events = []

    for line in log_lines:
        match = LOG_PATTERN.search(line)
        if match:
            event = {
                "timestamp": f"{match.group('month')} {match.group('day')} {match.group('time')}",
                "user": match.group("user"),
                "ip": match.group("ip")
            }
            events.append(event)

    return events
