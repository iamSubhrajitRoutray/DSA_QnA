'''Q) Find the Missing Number in the given Array.'''



''' BRUTE FORCE APPROACH -> '''

def missing_number(arr):
    
    n = len(arr)
    
    for i in range(1, n + 1):
        
        if i not in arr:
            return i


# Main/Driver code : 
array = [4, 6, 1, 8, 2, 3, 7]

print(array)

num = missing_number(array)

print(f' Missing number : {num}.')





''' DIRECT APPROACH -> '''

def missing_number(arr):
    
    n = len(arr) + 1
    
    num = (n * (n + 1)) // 2 - sum(arr)
    
    return num


# Main/Driver code : 
array = [1, 2, 3, 6, 5, 7]

print(array)

result = missing_number(array)

print(f'Missing number : {result}.')
