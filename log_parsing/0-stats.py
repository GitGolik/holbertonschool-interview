#!/usr/bin/python3
"""Log parsing: read stdin line by line and compute metrics."""

import signal
import sys

VALID_STATUS = {200, 301, 400, 401, 403, 404, 405, 500}

total_size = 0
status_counts = {code: 0 for code in VALID_STATUS}
lines_processed = 0


def print_stats():
    """Affiche les statistiques accumulées."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        count = status_counts[code]
        if count > 0:
            print(f"{code}: {count}")


def handle_interrupt(sig, frame):
    """Gère CTRL+C : affiche les stats puis sort proprement."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)


def parse_line(line: str):
    line = line.rstrip('\n')
    parts = line.split(' ')

    if len(parts) < 2:
        return None, None

    status_str = parts[-2]
    size_str = parts[-1]

    if not status_str.isdigit() or not size_str.isdigit():
        return None, None

    status = int(status_str)
    size = int(size_str)

    if status not in VALID_STATUS:
        return None, None

    if 'GET /projects/260 HTTP/1.1' not in line:
        return None, None
    if ' - [' not in line:
        return None, None
    if ']' not in line:
        return None, None

    ip_part = parts[0]
    ip_blocks = ip_part.split('.')
    if len(ip_blocks) != 4:
        return None, None
    for block in ip_blocks:
        if not block.isdigit():
            return None, None

    return status, size


def main():
    global total_size, lines_processed

    for line in sys.stdin:
        status, size = parse_line(line)
        if status is None:
            continue

        total_size += size
        status_counts[status] += 1
        lines_processed += 1

        if lines_processed % 10 == 0:
            print_stats()

    # À la fin du flux (EOF), on affiche une dernière fois
    print_stats()


if __name__ == "__main__":
    main()
