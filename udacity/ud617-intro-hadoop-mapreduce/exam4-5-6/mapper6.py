#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip_addr = data [0]
        cli_identity = data [1]
        cli_uname = data[2]
        req_time = data[3] + " " + data[4]
        req_line = data[5] + " " +  data[6] + " " + data[7]
        access_object = data[6]
        status_code = data [8]
        data_size = data[9]
        print access_object

