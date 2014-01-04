#Author: Dang Quang Vinh
#Date: 20140104
#Version: 1.0

#read input file
def readInputData ():
    f = open ('input.txt', 'r')
    input = []
    lines = f.read (). split ('\n')
    for line in lines:
        l = line.split(" ")
        l = [int(i) for i in l]
        input.append(l)
    return input
    
#parameter: 2 dimensions list
def solve (list):
    max = 0
    #for each list[i][i]
    #take care three directions: right, down and downward diagonal
    length = len (list)
    
    for i in range (length):
        for j in range (length):
            #for row:
            if j + 3 < length:
                tmp = list[i][j] * list[i][j + 1] * list[i][j + 2] * list[i][j + 3]
                if tmp > max:
                    max = tmp
            if i + 3 < length:
                tmp = list[i][j] * list[i + 1][j] * list[i + 2][j] * list[i + 3][j]
                if tmp > max:
                    max = tmp
            if i + 3 < length and j + 3 < length:
                tmp = list[i][j] * list[i + 1][j + 1] * list[i + 2][j + 2] * list[i + 3][j + 3]
                if tmp > max:
                    max = tmp
            if i >= 3 and j <= 16:
                tmp = list[i][j] * list[i - 1][j + 1] * list[i - 2][j + 2] * list[i - 3][j + 3]
                if tmp > max:
                    max = tmp
    return max
    
print solve (readInputData())