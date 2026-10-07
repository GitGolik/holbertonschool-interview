#!/usr/bin/python3
"""utf-8 validation"""


def validUTF8(data):
    """validation"""

    remaining = 0

    for d in data:
        byte = d & 0xFF  # si plus de 8 bits, on recup les 8 derniers

        if remaining == 0:
            if byte >> 7 == 0b0:  # 0xxxxxxx => 1 octet
                continue
            elif byte >> 5 == 0b110:  # 110xxxxx => 2 octets
                remaining = 1
            elif byte >> 4 == 0b1110:  # 1110xxxx => 3 octets
                remaining = 2
            elif byte >> 3 == 0b11110:  # 11110xxx => 4 octets
                remaining = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            remaining -= 1

    return remaining == 0
