#!/usr/bin/python3
"""Log parsing module"""
import sys


def print_stat(total_size, status_counts):
    """Print the stats"""
    print(f"File size: {total_size}")

    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def main():
    total_size = 0
    status_counts = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    line_counter = 0

    try:
        for line in sys.stdin:
            line_counter += 1

            parts = line.split()
            try:
                total_size += int(parts[-1])
                status_code = parts[-2]
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except (ValueError, IndexError):
                pass

            if line_counter % 10 == 0:
                print_stat(total_size, status_counts)

    except KeyboardInterrupt:
        print_stat(total_size, status_counts)
        sys.exit(0)

    print_stat(total_size, status_counts)


if __name__ == "__main__":
    main()
