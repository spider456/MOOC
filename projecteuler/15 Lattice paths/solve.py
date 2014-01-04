#http://www.robertdickau.com/lattices.html

import sys

def solve (n):
    list = []
    for i in range (n + 1):
        t = [None] * (n + 1)
        list.append (t)
        
    for i in range (n + 1):
        for j in range (n + 1):
            if i == 0 or j == 0:
                list [i][j] = 1
            else:
                list[i][j] = list [i - 1][j] + list [i][j - 1]
    
    return list[n][n]
    
print solve(int (sys.argv[1]))
    