#!/usr/bin/python3
"""Log parsing: read stdin line by line and compute metrics."""

import re
import signal
import sys

# Format attendu :
# <IP> - [<date>] "GET /projects/260 HTTP/1.1" <status> <size>
LOG_PATTERN = re.compile(
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'      # IP
    r' - \[([^\]]+)\]'                            # date entre crochets
    r' "GET /projects/260 HTTP/1\.1"'             # requête fixe
    r' (\d{3})'                                   # status code
    r' (\d+)$'                                    # file size
)

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


def parse_line(line: str) -> tuple:
    """
    Parse une ligne selon le format attendu.
    Retourne (status_code, file_size) ou (None, None) si invalide.
    """
    match = LOG_PATTERN.match(line.strip())
    if not match:
        return None, None

    status = int(match.group(3))
    size = int(match.group(4))

    if status not in VALID_STATUS:
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
