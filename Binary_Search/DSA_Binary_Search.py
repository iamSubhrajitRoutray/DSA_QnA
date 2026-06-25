'''BINARY SEARCH
Q)
You are given a sorted array of integers and a target,
your task is to search for the target in the given array.
Assume the given array does not contain any duplicate numbers.'''


'''ITERATIVE METHOD'''

def search(arr, target):
    
    arr.sort()
    
    n = len(arr)
    
    low = 0
    high = n - 1
    mid = (low + high) // 2
    
    while low <= high:
         
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            low += 1
        
        else:
            high -= 1
    
    return -1



'''RECURSIVE METHOD'''



def search(arr, low, high, target):
    
    arr.sort()
    
    n = len(arr)
    
    low = 0
    high = n - 1
    
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    
    elif arr[mid] < target:
        return search(arr, mid + 1, high, target)
    
    else:
        return search(arr, low, mid - 1, target)


    
'''TIME COMPLEXITY'''  # : log2_(N)

'''SPACE COMPLEXITY''' # : O(1)
    

    
    
            

