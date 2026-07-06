'''Peak element in Array
Q)
Given an array of length N, peak element is defined as the element greater than both of its neighbors.
Formally, if arr[i] is the peak element, arr[i - 1] < arr[i] and arr[i + 1] < arr[i]. Find the index(0-based) of a peak element in the array.
If there are multiple peak numbers, return the index of any peak number.'''



'''BRUTE-FORCE APPROACH'''


def peak(arr):
    
    n = len(arr)
    
    if n == 1:
        return arr[0]
    
    for i in range(0, n):
        
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            
            return arr[i]
        
    return "Element Not Found"


# Main/Driver code :

array = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]

answer = peak(array)

print(f"The peak element in array : {answer}")




'''OPTIMAL APPROACH'''


def peak_element(arr):
    
    n = len(arr)
    
    low, high = 0, n-1
    
    while low < high:
        
        mid = (low + high) // 2
        
        if arr[mid] < arr[mid + 1]:          # If mid element is less than next element in given array; (mid + 1)
            
            low  = mid + 1                 # Move to right half of the array
        
        else:
        
            high = mid                     # Move to left half of the array
            
    return arr[low]



# Main/Driver code :

array = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
print(f"Given array : {array}")

answer = peak_element(array)

print(f"The peak element : {answer}")
