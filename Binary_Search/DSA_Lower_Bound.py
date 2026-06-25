'''Implement Lower Bound :
Q)
Given a sorted array of N integers and an integer x,
write a program to find the lower bound of x.'''



def lower_bound(arr, target):
    
    low = 0
    high = len(arr) - 1
    
    l_b = len(arr)     # Initiating Lower Bound as leght of given array.
    
    while low <= high:
        
        mid = (low + high) // 2
        
        if arr[mid] >= target:
            
            l_b = mid
            
            high = mid - 1
            
        else:
            
            low = mid + 1
            
    return l_b



# Main/Driver code :

array = [1, 2, 2, 3]

x = 2  # Target element

result = lower_bound(array, x)

print(f"Given array : {array}")

print(f"The lower bound index is : {result}")
 
        
     
    