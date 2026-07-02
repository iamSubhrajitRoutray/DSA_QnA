'''Minimum in Rotated Sorted Array
Q)
Given an integer array arr of size N, sorted in ascending order (with distinct values), the array is rotated at any index which is unknown.
Find the minimum element in the array.'''




'''DIRECT APPROACH'''


def search(arr):
    
    min_ele = min(arr)
    
    return min_ele


# Main/Driver code:

array = [4, 5, 6, 7, 0, 1, 2, 3]

print(f"Given array : {array}")

ans = search(array)

print(f"Minimum element in array : {ans}")




'''BRUTE-FORCE APPROACH-1'''

def element(arr):
    
    min_ele = float("inf")
    
    for i in range(len(arr)):
        
        min_ele = min(min_ele, arr[i])
        
    return min_ele

# Main/Driver code:

array = [4, 5, 6, 7, 1, 2, 3]

print(f"Given array : {array}")

ans = element(array)

print(f"Minimum element in array : {ans}")




'''BRUTE-FORCE APPROACH-2'''


def element_search(arr):
    
    n = len(arr)
    
    min_ele = float("inf")   
    
    for i in range(0, n):
        temp = 0
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                temp = arr[i]
                min_ele = min(min_ele, temp)
    return min_ele



# Main/Driver code:

array = [4, 5, 6, 7, 2, 3]

print(f"Given array : {array}")

ans = element_search(array)

print(f"Minimum element in array : {ans}")



'''OPTIMAL APPROACH'''


def search_element(arr):
    
    n = len(arr)
    
    low, high = 0, n-1
    
    min_ele = float("inf")
    
    while low <= high:
        
        mid = (low + high) // 2
        
        if arr[low] <= arr[mid]:
            
            min_ele = min(min_ele, arr[low])
            
            high = mid - 1
            
        else:
            
            min_ele = min(min_ele, arr[mid])
            
            low = mid + 1
            
    return min_ele



# Main/Driver code:

array = [5, 6, 7, 1, 2, 3, 4]

print(f"Given array : {array}")

ans = element_search(array)

print(f"Minimum element in array : {ans}")


