#!/usr/bin/python3

"""
Log parsing script.

Reads stdin line by line, computes metrics, and prints statistics.
"""

import sys
import signal
from collections import defaultdict


def signal_handler(sig, frame):
    """Handles SIGINT signal."""
    print_stats()
    sys.exit(0)


def print_stats():
    """Prints statistics."""
    global total_size, status_counts
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")


def main():
    """Main function."""
    global total_size, status_counts, line_count
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0
    signal.signal(signal.SIGINT, signal_handler)

    for line in sys.stdin:
        parts = line.split('"')
        if len(parts) < 2:
            continue
        request = parts[1].split()
        if len(request) < 2:
            continue
        status_code = request[-1]
        if not status_code.isdigit():
            continue
        status_code = int(status_code)
        file_size = parts[-1].split()[-1]
        if not file_size.isdigit():
            continue
        file_size = int(file_size)
        total_size += file_size
        status_counts[status_code] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
    print_stats()


if __name__ == "__main__":
    main()
