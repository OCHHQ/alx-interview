#!/usr/bin/python3
def validUTF8(data):
    # Number of bytes remaining for the current character
    num_bytes = 0

    # Masks to determine the most significant bits
    mask1 = 1 << 7  # 10000000 in binary
    mask2 = 1 << 6  # 01000000 in binary

    for num in data:
        # Get the 8 least significant bits (simulate a byte)
        byte = num & 0xFF

        if num_bytes == 0:
            # Count the number of leading 1's to determine the byte length
            if byte & mask1 == 0:
                continue  # 1-byte character (0xxxxxxx)
            elif byte & (mask1 >> 1) == mask1:
                num_bytes = 1  # 2-byte character
            elif byte & (mask1 >> 2) == mask1:
                num_bytes = 2  # 3-byte character
            elif byte & (mask1 >> 3) == mask1:
                num_bytes = 3  # 4-byte character
            else:
                return False  # Invalid leading byte
        else:
            # Check if the byte is a valid continuation byte (10xxxxxx)
            if not (byte & mask1 and not (byte & mask2)):
                return False
        num_bytes -= 1

    return num_bytes == 0
