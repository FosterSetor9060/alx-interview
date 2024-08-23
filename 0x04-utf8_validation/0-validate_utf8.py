#!/usr/bin/python3
"""UTF-8 validation module"""


def validUTF8(data):
    """
    Validate if a list of integers represents valid UTF-8 encoded data.
    
    Args:
        data (list): A list of integers representing the data to be validated.
        
    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """
    num_bytes = 0

    for byte in data:
        # Convert to binary and keep only the last 8 bits
        bin_rep = format(byte, '08b')

        if num_bytes == 0:
            # Determine the number of bytes in the sequence
            if bin_rep[0] == '1':
                num_bytes = len(bin_rep.split('0')[0])

            # Single-byte character
            if num_bytes == 0:
                continue

            # Invalid initial byte if it starts with '10' or has more than 4 leading '1's
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (bin_rep[0:2] == '10'):
                return False

        num_bytes -= 1

    return num_bytes == 0

