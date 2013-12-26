# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(input):
    if len(input) == 0:
        return None
    
    #longest repetition so far
    max_len = 0
    #id of the start point of the longest repetition so far
    id_max = 0
    #length of current repetition
    cur_len = 0
    #start id of current repetition
    start_id = 0
    
    for i in range(len(input)):
        if i == 0:
            cur_len = 1
        else:
            if input[i] == input[start_id]:
                cur_len += 1
                
                #More optimization if only update after end of repetition list
                #In this exercise, it does not matter
                if cur_len > max_len:
                    max_len = cur_len
                    id_max = start_id
            else:
                start_id = i
                cur_len = 1
    return input [id_max]
                



#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

