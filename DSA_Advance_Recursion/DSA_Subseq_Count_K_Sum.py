'''Count all subsequences with sum K
Q)
Given an array nums and an integer k.
Return the number of non-empty subsequences of nums such that the sum of all elements in the subsequence is equal to k.'''


def backtrack(index, total):
    
    if total == target:
        return 1
    
    elif total > target:
        return 0
    
    if index >= len(array):
        return 0
    
    Sum = total + array[index]
    
    pick = backtrack(index + 1, Sum)
    
    Sum = total
    
    not_pick = backtrack(index + 1, Sum)
    
    return pick + not_pick
    


# MAIN/DRIVER CODE:

array = [5, 9, 4]

target = 9

answer = backtrack(0, 0)

print(f"\nNumber of subsequence having sum {target} : {answer}\n")