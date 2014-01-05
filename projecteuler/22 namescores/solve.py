import sys

def readInputData (filename):
    f = open (filename, 'r')
    input = []
    lines = f.read (). split (',')
    for word in lines:
        t = word[1:-1]
        input.append(t)
    input.sort()
    return input
    
def wordValue (str):
    sum = 0
    for i in range (len(str)):
        sum += ord (str[i]) - ord('A') + 1
    return sum
    
def solve (M):
    sum = 0
    for i in range (len(M)):
        sum += (i + 1) * wordValue (M[i])
    return sum
    
print solve (readInputData (sys.argv[1]))