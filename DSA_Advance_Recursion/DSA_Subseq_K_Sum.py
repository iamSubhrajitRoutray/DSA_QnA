'''Print all subsequences with sum K
Q)
Given an array nums and an integer k.
Return the number of non-empty subsequences of nums such that the sum of all elements in the subsequence is equal to k.'''


def backtrack(index, total, subset):
    
    if total == target:
        result.append(subset.copy())
        return
    
    elif total > target:
        return
    
    if index >= len(array):
        return
    
    subset.append(array[index])
    
    Sum = total + array[index]
    
    backtrack(index + 1, Sum, subset)
    
    e = subset.pop()
    
    Sum = Sum - e
    
    backtrack(index + 1, Sum, subset)
    
    


# MAIN/DRIVER CODE:

array = [5, 9, 4]

target = 9

result = []

subset = []


backtrack(0, 0, subset)

for subseq in result:
    
    print(f"{subseq}", end=" ")
    
print()