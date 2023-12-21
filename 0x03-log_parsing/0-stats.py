#!/usr/bin/python3
""" A script to pass logs to """


import sys

status_counts = {'200': 0, '301': 0, '400': 0, '401': 0,
                 '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
line_counter = 0

try:
    for line in sys.stdin:
        line_items = line.split(" ")
        if len(line_items) > 4:
            http_status = line_items[-2]
            size = int(line_items[-1])
            if http_status in status_counts:
                status_counts[http_status] += 1
            total_size += size
            line_counter += 1

        if line_counter == 10:
            line_counter = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(status_counts.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_counts.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
