#!/usr/bin/python3
"""utf-8 validation"""


def validUTF8(data):
    """validation"""

    remaining = 0

    for d in data:
        byte = d&0xff # si plus de 8 bits, on recup les 8 derniers

        if remaining == 0:
            if byte >> 7 == 0b0: # 1xxxxxxx => recup le 1
                continue
            elif byte >> 5 == 0b110: 
                remaining = 1
            elif byte >> 4 == 0b1110: 
                remaining = 2
            elif byte >> 3 == 0b11110: 
                remaining = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            remaining -= 1

    return remaining == 0
