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
        binary_rep = format(byte, '#010b')[-8:]

        if num_bytes == 0:
            if binary_rep[0] == '1':
                num_bytes = len(binary_rep.split('0')[0])

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (binary_rep[0:2] == '10'):
                return False

        num_bytes -= 1

    return num_bytes == 0

