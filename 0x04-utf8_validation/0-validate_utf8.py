#!/usr/bin/python3
"""
Module for UTF-8 validation.
"""


def validUTF8(data):
    """valid UTF"""
    n_bytes = 0

    for num in data:
        binary = format(num, '#010b')[-8:]

        if n_bytes == 0:
            if binary[0] == '0':
                continue

            for bit in binary:
                if bit == '1':
                    n_bytes += 1
                else:
                    break

            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (binary[0] == '1' and binary[1] == '0'):
                return False

        n_bytes -= 1

    return n_bytes == 0
