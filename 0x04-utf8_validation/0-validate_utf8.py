#!/usr/bin/python3
"""
Module to validate if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    # The number of bytes remaining for the current UTF-8 character
    num_bytes = 0

    # Masks to check the structure of each byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for number in data:
        # Only use the 8 least significant bits of the number
        byte = number & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if byte & mask1 == 0:
                continue  # 1-byte character: 0xxxxxxx
            elif byte & (mask1 >> 1) == mask1:
                num_bytes = 1  # 2-byte character: 110xxxxx
            elif byte & (mask1 >> 2) == mask1:
                num_bytes = 2  # 3-byte character: 1110xxxx
            elif byte & (mask1 >> 3) == mask1:
                num_bytes = 3  # 4-byte character: 11110xxx
            else:
                return False  # Invalid leading byte
        else:
            # Check if the byte is a valid continuation byte: 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    return num_bytes == 0
