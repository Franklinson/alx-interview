#!/usr/bin/python3
""" A script to pass logs to """

import sys

# Store the count of all status codes in a dictionary
status_code_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                      '404': 0, '405': 0, '500': 0}

total_file_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_parts = line.split(" ")

        if len(line_parts) > 4:
            status_code = line_parts[-2]
            file_size = int(line_parts[-1])

            # Check if the status code exists in
            # the dictionary and increment its count
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            # Update total file size
            total_file_size += file_size

            # Update count of lines
            line_count += 1

        if line_count == 10:
            line_count = 0  # Reset line count
            print('Total File Size: {}'.format(total_file_size))

            # Print out status code counts
            for code, count in sorted(status_code_counts.items()):
                if count != 0:
                    print('{}: {}'.format(code, count))

            # Reset status code counts for the next iteration
            status_code_counts = {'200': 0, '301': 0, '400': 0, '401': 0,
                                  '403': 0, '404': 0, '405': 0, '500': 0}

except Exception as err:
    pass

finally:
    print('Total File Size: {}'.format(total_file_size))
    for code, count in sorted(status_code_counts.items()):
        if count != 0:
            print('{}: {}'.format(code, count))
