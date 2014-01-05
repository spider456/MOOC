import sys

def readInputData (filename):
    f = open (filename, 'r')
    input = []
    lines = f.read (). split ('\n')
    for line in lines:
        l = line.split(" ")
        l = [int(i) for i in l]
        input.append(l)
    return input
    
def solve (M):
    l = len (M)
    for i in range (l):
        for j in range (l - i - 1):
            M[l - i - 2][j] = max (M[l - i - 2][j] + M[l - i - 1][j], M[l - i - 2][j] + M[l - i - 1][j + 1])
    return M[0][0]
    
print solve (readInputData (sys.argv[1]))