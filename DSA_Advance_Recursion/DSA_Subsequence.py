'''Q)
Find all the subsequene in a given array by recursion and backtracking'''


def backtrack(index, result, subset):
    
    if index >= len(array):
        result.append(subset.copy())
        return
    
    subset.append(array[index])
    
    backtrack(index + 1, result, subset)
    
    subset.pop()
    
    backtrack(index + 1, result, subset)
    
    
    
# MAIN/DRIVER CODE:

array = [5, 9, 4]
result = []
subset = []

backtrack(0, result, subset)

for subseq in result:
    print(f"{subseq}", end = " ")
    
print()



