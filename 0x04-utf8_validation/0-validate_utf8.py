#!/usr/bin/python3

""" Check if if a given data set represents a valid UTF-8 encoding """


def validUTF8(data):
    """Variable to track the number of consecutive leading bits set to 1"""
    num_leading_ones = 0

    # Iterate through each byte in the data
    for byte in data:
        # Check if the current byte is a continuation byte (starts with '10')
        if num_leading_ones > 0:
            if (byte >> 6) == 0b10:
                num_leading_ones -= 1
            else:
                return False
        else:
            # Count the number of consecutive leading bits set to 1
            while (byte >> (7 - num_leading_ones)) & 1 == 1:
                num_leading_ones += 1

            # For a single-byte character, num_leading_ones will be 0
            if num_leading_ones == 1 or num_leading_ones > 4:
                return False

    # Check if the last character is complete
    return num_leading_ones == 0
