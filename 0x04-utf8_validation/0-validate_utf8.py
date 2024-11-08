#!/usr/bin/python3
"""
Module to validate if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    num_bytes = 0  # Number of bytes left to process for a character

    # Masks to check the structure of each byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for number in data:
        # Only consider the last 8 bits of the number (1 byte)
        byte = number & 0xFF

        if num_bytes == 0:  # No ongoing multi-byte character
            # Determine the number of bytes in the current UTF-8 character
            if byte & mask1 == 0:  # 1-byte character: 0xxxxxxx
                continue
            elif byte & (mask1 >> 1) == mask1:  # 2-byte character: 110xxxxx
                num_bytes = 1
            elif byte & (mask1 >> 2) == mask1:  # 3-byte character: 1110xxxx
                num_bytes = 2
            elif byte & (mask1 >> 3) == mask1:  # 4-byte character: 11110xxx
                num_bytes = 3
            else:
                return False  # Invalid leading byte
        else:
            # Check if the byte is a valid continuation byte: 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    return num_bytes == 0  # Return True if all bytes are processed correctly
