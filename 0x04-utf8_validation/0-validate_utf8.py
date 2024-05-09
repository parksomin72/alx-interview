#!/usr/bin/python3
"""
Checks if a given data set represents a valid UTF-8 encoding.
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list of int): List of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise.
    """
    # Number of bytes expected for the current UTF-8 character
    num_bytes = 0

    for byte in data:
        # If num_bytes is 0, it means we are starting a new UTF-8 character
        if num_bytes == 0:
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7) != 0:
                return False  # Invalid UTF-8 start byte
        else:
            if (byte >> 6) != 0b10:
                return False  # Invalid UTF-8 following byte
            num_bytes -= 1

    # If num_bytes is not zero at the end, it means the data is incomplete
    return num_bytes == 0

# Test cases
if __name__ == "__main__":
    data1 = [65]
    print(validUTF8(data1))  # True

    data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data2))  # True

    data3 = [229, 65, 127, 256]
    print(validUTF8(data3))  # False

