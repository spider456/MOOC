#author: Dang Quang Vinh
#date: 2014-01-04

import time

def collatzLen (n):
    count = 1
    #print n,
    #print '->',
    if n == 1:
        return 1
        
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        #print n,
        #print '->',
        count += 1
    
    #print ' '
    return count
    
def solve (n):
    maxLen = 0
    index_max = 0
    for i in range (1, n + 1):
        #print "Processing sequence: " + str(i)
        length = collatzLen (i)
        if maxLen < length:
            maxLen = length
            index_max = i
    return maxLen
    
start = time.time ()
print "\nmax length:" + str(solve (1000000))
elapsed = time.time() - start
print elapsed