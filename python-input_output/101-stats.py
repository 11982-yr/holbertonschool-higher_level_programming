#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics:
- Total file size
- Number of lines by status code
Prints stats every 10 lines and on keyboard interruption.
"""

import sys


def print_stats(total_size, status_counts):
    """Print the required statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] != 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    total_size = 0
    line_count = 0
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status_counts = {code: 0 for code in valid_codes}

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) >= 2:
                status_code = parts[-2]
                file_size = parts[-1]

                if status_code in status_counts:
                    status_counts[status_code] += 1

                try:
                    total_size += int(file_size)
                except (ValueError, TypeError):
                    pass

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

        # Print remaining stats at EOF (for inputs not multiple of 10)
        if line_count > 0 and line_count % 10 != 0:
            print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise


if __name__ == "__main__":
    main()
