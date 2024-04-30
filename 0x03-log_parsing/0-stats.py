#!/usr/bin/python3

import sys
import re

# Initialize variables
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Define constants
INPUT_FORMAT_REGEX = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
VALID_STATUS_CODES = [200, 301, 400, 401, 403, 404, 405, 500]

try:
    for line in sys.stdin:
        line = line.strip()
        
        # Match against input format using regular expressions
        match = re.match(INPUT_FORMAT_REGEX, line)
        if match:
            ip_address, date, status_code, file_size = match.groups()
            
            # Update total file size
            total_size += int(file_size)
            
            # Update status code counts
            status_code = int(status_code)
            if status_code in VALID_STATUS_CODES:
                status_counts[status_code] += 1
            
            # Increment line count
            line_count += 1
            
            # Check if 10 lines have been processed
            if line_count % 10 == 0:
                print(f'Total file size: File size: {total_size}')
                for code in sorted(status_counts.keys()):
                    if status_counts[code] > 0:
                        print(f'{code}: {status_counts[code]}')
                print()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print(f'Total file size: File size: {total_size}')
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f'{code}: {status_counts[code]}')
    sys.exit(0)
