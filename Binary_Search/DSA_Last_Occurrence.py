'''Last occurrence in a sorted array
Q)
Given a sorted array of N integers, write a program to find the index of the last occurrence of the target key.
If the target is not found then return -1. Note: Consider 0 based indexing'''



''' BRUTE-FORCE APPROACH '''

def occurrence(arr, target):
    
    n = len(arr)
    
    for i in range(n-1,-1,-1):
        if arr[i] == target:
            return i


# Main/Driver Code:

array = [3, 4, 13, 13, 13, 20, 40]

print(f"Given array : {array}")

x = 13

index = occurrence(array, x)

print(f"Last occurrence of {x} is at index {index}")  




''' OPTIMAL APPROACH '''

def occurrence(arr, target):
    
    n = len(arr)
    
    start = 0
    end = n - 1
    
    ans = -1
    
    while start <= end:
        
        mid = (start + end) // 2
        
        if arr[mid] == target:
            ans = mid
            start = mid + 1
            
        elif arr[mid] > target:
            end = mid - 1
        
        else:
            start = mid + 1
            
    return ans


# Main/Driver Code:

array = [3, 4, 13, 13, 13, 20, 40]

print(f"Given array : {array}")

x = 13

index = occurrence(array, x)

print(f"Last occurrence of {x} is at index {index}")  

