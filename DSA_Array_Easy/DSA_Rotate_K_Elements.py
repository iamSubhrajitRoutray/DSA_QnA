'''Q) Given an array of integers, rotating array of elements by k elements either left or right.'''


''' BRUTE FORCE APPROACH -> '''

def rotate_array(arr, k, direction):
    
    n = len(arr)
    
    k = k % n
    
    if n == 0 and k == 0:
        return arr
    
    if direction == 'left':
        
        for _ in range(0, k):
            
            e = arr.pop(0)             # We pop the specific element from the array and stored it in var. 'e'
            
            arr.insert(n - 1, e)       # Then insert the pop elements from e to given index 
            
                  
    if direction == 'right':
        
        for _ in range(0, k):
            
            e = arr.pop()            # By default the pop argumnet takes arr[-1] value i.e n-1 index value.
            
            arr.insert(0, e)         # Insert the pop element from e to the given index.
            
    print(arr)
     

# Main/Driver code :  
array = [1, 2, 3, 4, 5, 6, 7]

rotate_array(array, 2,'left')



''' BETTER APPROACH '''

def rotate_array(arr, k):
 
    n = len(arr)
    
    k = k % n
    
    # By the use of default slicing, we can split and slice/cut the array by the k and n value
    arr[ : ] = arr[n - k :] + arr[: n - k]
    
    print(arr)
    
# Main/Driver code :  
array = [1, 2, 3, 4, 5, 6, 7]

rotate_array(array, 2)






''' OPTIMAL APPROACH -> '''

# function to reverse the given array.
def reverse(arr, start, end):
    # Set the start and end according to the index by the given lenght of array and k.
    while start < end:            
    
        arr[start], arr[end] = arr[end], arr[start]      # Swapping the elements in the array.
    
        start += 1
        end -= 1
    
# To rotate the array by the k terms.
def rotate_array(arr, k, direction): 
   
    n = len(arr) 
    
    k = k % n
    
    if n == 0 and k == 0:           # Base case check.
        return arr
    
    if direction == 'right':
        
        reverse(arr, 0, n - 1)      # Reverse the whole array
        
        reverse(arr, 0, k - 1)      # Reverse the first k elements in the array
        
        reverse(arr, k, n - 1)      # Reverse the rest n-k elements in the array
    
    
    elif direction == 'left': 
        
        reverse(arr, 0, k - 1)      # Reverse the first k elements in the array 
        
        reverse(arr, k, n - 1)      # Reverse the rest n-k elements in the array
        
        reverse(arr, 0, n - 1)      # Reverse the whole array
        
    print(arr)


# Main/Driver code :  
array = [1, 2, 3, 4, 5, 6, 7]

rotate_array(array, 2,'left')
