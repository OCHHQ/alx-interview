#!/usr/bin/python3
import sys
import signal
from collections import defaultdict

# Initialize variables
total_size = 0
status_counts = defaultdict(int)
line_count = 0


def print_stats():
    global total_size, status_counts
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")


def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


def main():
    global total_size, status_counts, line_count
    signal.signal(signal.SIGINT, signal_handler)
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        # Validate input format
        if len(parts) != 10 or parts[6] != 'HTTP/1.1"':
            continue
        # Extract status code and file size
        status_code = int(parts[8])
        file_size = int(parts[9])
        # Update totals
        total_size += file_size
        status_counts[status_code] += 1
        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()
    # Print final stats
    print_stats()


if __name__ == "__main__":
    main()
