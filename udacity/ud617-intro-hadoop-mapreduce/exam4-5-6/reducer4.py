#!/usr/bin/python

import sys

hitsCount = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    ip_addr, access_object = data_mapped

    if access_object == "/assets/js/the-associates.js":
        hitsCount += 1

print  hitsCount

