#!/usr/bin/python3
"""UTF-8 validator"""


def validUTF8(data):
    """
    Check if a given list of integers represents a valid UTF-8 encoding.
    
    Args:
        data (list): A list of integers representing the data to validate.
        
    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """
    num_bytes = 0

    for byte in data:
        # Get the binary representation of the byte, keeping only the last 8 bits
        binary_rep = format(byte, '#010b')[-8:]

        if num_bytes == 0:
            # Count the number of leading 1's to determine the number of bytes in this UTF-8 character
            if binary_rep[0] == '1':
                num_bytes = len(binary_rep.split('0')[0])

            # 1-byte character (0xxxxxxx)
            if num_bytes == 0:
                continue

            # Invalid scenarios
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
        
            if not (binary_rep[0:2] == '10'):
                return False

        num_bytes -= 1

    return num_bytes == 0

