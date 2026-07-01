'''Search Element in Rotated Sorted Array II
Q)
Given an integer array arr of size N, sorted in ascending order (may contain duplicate values) and a target value k.
Now the array is rotated at some pivot point unknown to you.
Return True if k is present and otherwise, return False.'''



'''BRUTE-FORCE APPROACH'''


def search_element(arr, target):
    
    for i in range(len(arr)):
    
        if arr[i] == target:
            
            return True
    
    return False


# Main/Driver code:

arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
k = 3

print(search_element(arr, k))



'''OPTIMAL APPROACH'''


def serach_element(arr, target):
    
    low = 0
    
    high = len(arr) - 1
    
    while low <= high:
        
        mid = (low + high) // 2
        
        if arr[mid] == target:
            
            return True
        
        if arr[low] == arr[mid] == arr[high]:

            low += 1
            
            high -= 1
            
            continue
        
        if arr[low] <= arr[mid]:

            if arr[low] <= target <= arr[mid]:

                high = mid - 1

            else:

                low = mid + 1

        else:

            if arr[mid] <= target <= arr[high]:

                low = mid + 1

            else:

                high = mid - 1

        return True

    return False


# Main/Driver code:

arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
k = 5

print(search_element(arr, k))
