#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Check if the data set represents a valid UTF-8 encoding.
    """
    num_bytes = 0  # Number of bytes in the current UTF-8 character

    # Masks to check the leading bits of a byte
    mask1 = 1 << 7   # 10000000
    mask2 = 1 << 6   # 01000000

    for byte in data:
        if num_bytes == 0:
            # Check how many leading 1s are in the first byte
            mask = 1 << 7
            while byte & mask:
                num_bytes += 1
                mask >>= 1

            # 1-byte character
            if num_bytes == 0:
                continue

            # Invalid cases
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the byte is a valid continuation byte (10xxxxxx)
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0


# Test cases
if __name__ == "__main__":
    data1 = [65]  # Valid UTF-8
    print(validUTF8(data1))  # True

    data2 = [229, 65, 127, 256]  # Invalid UTF-8
    print(validUTF8(data2))  # False

