#!/usr/bin/python

import sys

hitsCount = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    ip_addr, access_object = data_mapped

    if ip_addr == "10.99.99.186":
        hitsCount += 1

print  hitsCount

