LIMIT = 28123

def isAbundant (n):
    sum = 0
    for i in range (1, n/2 + 1):
        if n % i == 0:
            sum += i
    if sum > n:
        return True
    return False

def listOfAbundantNumbers ():
    lst = []
    for i in range (LIMIT + 1):
        if isAbundant (i) == True:
            lst.append (i)
    return lst
    
def listOfAbundantSum ():
    lst = listOfAbundantNumbers ()
    result = []
    for i in range (len (lst)):
        for j in range (0, len (lst)):
            result.append (lst[i] + lst[j])
    return list (set (result))
    
def solve ():
    full_list = range (1, LIMIT + 1)
    sum = 0
    for i in list (set (full_list) - set(listOfAbundantSum ())):
        sum += i
    return sum
        
def test ():
    assert isAbundant (12) == True
    assert isAbundant (10) == False

test ()
print solve ()