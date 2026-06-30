'''Search Element in a Rotated Sorted Array
Q)
Given an integer array nums, sorted in ascending order (with distinct values) and a target value k. 
he array is rotated at some pivot point that is unknown.
Find the index at which k is present and if k is not present return -1.'''




'''BRUTE-FORCE APPROACH'''


def search_element(arr,k):
    
    n = len(arr)
    
    for i in range(n):
    
        if arr[i] == k:
    
            return True
    
    return False


# Main/Driver code:

array = [4, 5, 6, 7, 0, 1, 2]

k = 1

print(search_element(array,k))




'''OPTIMAL APPROACH'''


def search_element(arr,k):

    low = 0

    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == k:

            return True

        if arr[low] <= arr[mid]:

            if arr[low] <= k <= arr[mid]:

                high = mid - 1

            else:

                low = mid + 1
                
        else:

            if arr[mid] <= k <= arr[high]:

                low = mid + 1

            else:

                high = mid - 1

        return True

    return False


# Main/Driver code:

array = [4, 5, 6, 7, 0, 1, 2]

k = 1

print(search_element(array,k))

