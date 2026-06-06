'''Q) Given an integer array nums, rotate the array to the left by one.'''

def rotate_element(arr):
    
    n = len(arr)
    
    temp  = arr[0]              # Store the first element in a temporary variable
    
    for i in range(1, n):
        
        arr[i - 1] = arr[i]       # Shift elements to the left
    
    arr[-1] = temp              # Place the first element at the end
            
    print(f'Updated array : {arr}')


# Main/Driver code : 
array = [1, 2, 3, 4, 5, 6]

rotate_element(array)