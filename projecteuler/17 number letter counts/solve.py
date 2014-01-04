# http://stackoverflow.com/questions/8982163/how-do-i-tell-python-to-convert-integers-into-words
import sys

delimiter = "" #use for this problem

def handel_upto_99(number):
    predef={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"hundred",100000:"lakh",10000000:"crore",1000000:"million",1000000000:"billion"}
    if number in predef.keys():
        return predef[number]
    else:
        return predef[(number/10)*10]+ delimiter +predef[number%10]
    
def return_bigdigit(number,devideby):
    predef={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"hundred",1000:"thousand",100000:"lakh",10000000:"crore",1000000:"million",1000000000:"billion"}
    if devideby in predef.keys():
        return predef[number/devideby]+ delimiter +predef[devideby]
    else:
        devideby/=10
        return handel_upto_99(number/devideby)+ delimiter +predef[devideby]
    
def mainfunction(number):
    dev={100:"hundred",1000:"thousand",100000:"lakh",10000000:"crore",1000000000:"billion"}
    if number is 0:
        return "Zero"
    if number<100:
        result=handel_upto_99(number)

    else:
        result=""
        while number>=100:
            devideby=1
            length=len(str(number))
            for i in range(length-1):
                devideby*=10
            if number%devideby==0:
                if devideby in dev:
                    return handel_upto_99(number/devideby)+delimiter+ dev[devideby]
                else:
                    return handel_upto_99(number/(devideby/10))+delimiter+ dev[devideby/10]
            res=return_bigdigit(number,devideby)
            result=result+delimiter+res
            if devideby not in dev:
                number=number-((devideby/10)*(number/(devideby/10)))
            number=number-devideby*(number/devideby)

        if number <100:
            result = result + delimiter + "and" + delimiter + handel_upto_99(number)
    return result
    
def test ():
    assert len (mainfunction (342)) == 23
    assert len (mainfunction (115)) == 20

def solve (n):
    sum = 0
    for i in range (1, n + 1):
        sum += len (mainfunction (i))
    return sum

print solve (int(sys.argv[1]))