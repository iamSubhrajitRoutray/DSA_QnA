'''Floor and Ceil in Sorted Array
Q)
You're given an sorted array arr of n integers and an integer x.
Find the floor and ceiling of x in arr[0..n-1].'''

# The floor of x is the largest element in the array <= target.
# The ceiling of x is the smallest no. in array >= target



def floor_ceil(arr,target):
    
    low=0
    
    high=len(arr)-1
    
    floor = ceil = -1
    
    while low <= high:
    
        mid = (low+high) // 2
    
        if arr[mid] == target:
            
            return [arr[mid], arr[mid]]
        
        elif arr[mid] > target:
            
            ceil = arr[mid]
            
            high = mid - 1   
    
        else:
            
            floor = arr[mid]
            
            low = mid + 1
    
    return [floor, ceil]


# Main/Driver code:

array = [3, 4, 4, 7, 8, 10]
x = 6

answer = floor_ceil(array, x)
print(answer)
         
            