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
        line_count += 1
        parts = line.split()

        if len(parts) != 10 or parts[6] != 'HTTP/1.1"':
            continue

        status_code = int(parts[8])
        file_size = int(parts[9])
        total_size += file_size
        status_counts[status_code] += 1

        if line_count % 10 == 0:
            print_stats()
    print_stats()


if __name__ == "__main__":
    main()
