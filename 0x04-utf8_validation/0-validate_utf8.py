#!/usr/bin/python3

""" Check if if a given data set represents a valid UTF-8 encoding """


def validUTF8(data):
    num_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        byte = num & 0xFF

        if num_bytes == 0:
            if (byte & mask1) == 0:
                num_bytes = 0
            elif (byte & mask2) == 0:
                return False
            else:
                num_leading_ones = 0
                while (byte & mask1) != 0:
                    num_leading_ones += 1
                    byte <<= 1
                num_bytes = num_leading_ones
        else:
            if (byte & mask1) == 0 or (byte & mask2) != 0:
                return False
            num_bytes -= 1

    return num_bytes == 0
