'''Check if there exists a subsequence with sum K
Q)
Given an array nums and an integer k.
Return true if there exist subsequences such that the sum of all elements in subsequences is equal to k else false.'''


def backtrack(index, total):
    
    if total == target:
        return True
    
    elif total > target:
        return False
    
    if index >= len(array):
        return False

    Sum = total + array[index]
    
    pick = backtrack(index+1, Sum)
    
    if pick == True:
        return True
    
    Sum = total
    
    not_pick = backtrack(index+1, Sum)
    
    return not_pick
    
    
    

# MAIN/DRIVER CODE:

array = [5, 9, 4]

target = 9

result = []

subset = []

answer = backtrack(0, 0)

print(f"\n{answer}\n")
