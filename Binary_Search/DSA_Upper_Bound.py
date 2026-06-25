'''Implement Upper Bound :
Q)
Given a sorted array of N integers and an integer x, write a program to find the upper bound of x.'''

# Q)What is Upper Bound?

# :- The upper bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than the given key i.e. x.
# The upper bound is the smallest index, ind, where arr[ind] > x.



def upper_bound(arr, target):
    
    low = 0
    high = len(arr) - 1
    
    u_b = len(arr)  # Initiating Upper Bound as leght of given array.

    while low <= high:
        
        mid = (low + high) // 2
        
        if arr[mid] > target:
            
            u_b = mid
            
            high = mid - 1
            
        else:
            low = mid + 1
            
            
    return u_b



# Main/Driver code :

array = [1, 2, 2, 3]

x = 2  # Target element

result = upper_bound(array, x)

print(f"Given array : {array}")

print(f"The upper bound index is : {result}")




