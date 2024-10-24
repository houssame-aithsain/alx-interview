#!/usr/bin/python3
"""stats module."""
import sys


total_size = 0
status_counts = {}
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0


def print_stats():
    """Print the accumulated metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Validate line format and extract necessary data
        if len(parts) > 6:
            status_code = parts[-2]
            file_size = parts[-1]

            # Update file size
            try:
                total_size += int(file_size)
            except ValueError:
                continue

            # Update status code count
            if status_code in valid_codes:
                if status_code not in status_counts:
                    status_counts[status_code] = 0
                status_counts[status_code] += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    pass

# Print final statistics when script ends
print_stats()
