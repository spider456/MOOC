#!/usr/bin/python

import sys

hitsCount = 0
highestObject = None
highestHitsCount = 0
old_object = None

for line in sys.stdin:
    #data_mapped = line.strip().split("\t")
    #if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
    #    continue

    access_object = line
    
    if old_object and old_object != access_object:
        if highestHitsCount < hitsCount:
            highestHitsCount = hitsCount
            highestObject = old_object
            print "Last object = " + highestObject
            print "Last Count = " + str (highestHitsCount)
        hitsCount = 0
        old_object = access_object
    
    old_object = access_object
    hitsCount += 1

print highestObject
print highestHitsCount

