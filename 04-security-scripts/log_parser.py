"""
log_parser.py

Parses an authentication log file (Linux-style auth.log format) to identify
failed login attempts and flag source IPs that exceed a suspicious threshold —
a simplified version of what a SOC analyst does when triaging brute-force alerts.

Usage:
    python3 log_parser.py sample_auth.log
    python3 log_parser.py sample_auth.log --threshold 3
"""

import argparse
import re
from collections import Counter

FAILED_LOGIN_PATTERN = re.compile(
    r"Failed password for (?:invalid user )?(?P<user>\S+) from (?P<ip>\d+\.\d+\.\d+\.\d+)"
)


def parse_log(filepath: str):
    """Return a list of (user, ip) tuples for every failed login line found."""
    failures = []
    with open(filepath, "r") as f:
        for line in f:
            match = FAILED_LOGIN_PATTERN.search(line)
            if match:
                failures.append((match.group("user"), match.group("ip")))
    return failures


def summarize(failures, threshold: int = 5):
    ip_counts = Counter(ip for _, ip in failures)
    user_counts = Counter(user for user, _ in failures)

    print(f"Total failed login attempts: {len(failures)}\n")

    print("Top source IPs by failed attempts:")
    for ip, count in ip_counts.most_common(10):
        flag = "  <-- SUSPICIOUS" if count >= threshold else ""
        print(f"  {ip:<16} {count:>4} attempts{flag}")

    print("\nTop targeted usernames:")
    for user, count in user_counts.most_common(10):
        print(f"  {user:<16} {count:>4} attempts")


def main():
    parser = argparse.ArgumentParser(description="Parse auth logs for failed login attempts.")
    parser.add_argument("logfile", help="Path to the auth log file")
    parser.add_argument("--threshold", type=int, default=5,
                         help="Flag IPs with at least this many failed attempts (default: 5)")
    args = parser.parse_args()

    failures = parse_log(args.logfile)
    summarize(failures, threshold=args.threshold)


if __name__ == "__main__":
    main()
