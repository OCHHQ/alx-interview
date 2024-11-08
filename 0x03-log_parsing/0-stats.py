#!/usr/bin/python3

"""
Log parsing script.

Reads stdin line by line, computes metrics, and prints statistics.
"""

import sys
import signal
from collections import defaultdict

# Global variables for total size and status code counts
total_size = 0
status_counts = defaultdict(int)
line_count = 0

# Allowed status codes
valid_status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}


def print_stats():
    """Prints accumulated statistics."""
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")


def parse_line(line):
    """Parses a line of the log and updates metrics."""
    global total_size, status_counts
    try:
        parts = line.split()
        # Ensure the line has enough parts
        if len(parts) < 7:
            return
        status_code = parts[-2]
        file_size = parts[-1]
        # Check if status code and file size are valid
        if status_code in valid_status_codes and file_size.isdigit():
            status_counts[status_code] += 1
            total_size += int(file_size)
    except Exception:
        pass  # Ignore any parsing errors


def signal_handler(sig, frame):
    """Handles keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)


def main():
    """Main function to read from stdin and parse lines."""
    global line_count
    signal.signal(signal.SIGINT, signal_handler)
    try:
        for line in sys.stdin:
            parse_line(line.strip())
            line_count += 1
            if line_count % 10 == 0:
                print_stats()
        print_stats()  # Print final statistics
    except KeyboardInterrupt:
        print_stats()
        sys.exit(0)


if __name__ == "__main__":
    main()
