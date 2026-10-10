'''Given an array of N integers, write a program to implement the Bubble Sorting algorithm.'''

'''BRUTE FORCE METHOD ->'''

def bubble_sort(arr):
    
    n = len(arr)     # Gives us the lenght of the array.
    
    # Loop for bubble sort
    for i in range(n-2, -1, -1):       # Initiate val of i as n-2 acc. to index val & keep on decrement.
        
        for j in range(0, i + 1):        # val j to be run from 0 to i+1 val.
            
            if arr[j] > arr[j + 1]:      # If val of j > j+1 (its adjacent) val; then SWAP.
                
                arr[j], arr[j + 1] = arr[j + 1], arr[j]     # Swapping the vlaue in array.
                
    print(arr)
 

# Main/Driver code :   
array = [5, 2, 6, 8, 1, 4, 9]

bubble_sort(array)



'''OPTIMAL METHOD ->'''

def bubble_sort(arr):
    
    n = len(arr)     # Gives us the lenght of the array.
    
    # Variable to check if swapping is done or not.
    
    # By default we take it as FALSE; which says no swapping has been done yet.
    is_swap = False
    
    #loop for bubble sort
    for i in range(n-2, -1, -1):         # We initiate val of i as n-2 acc. to index val & keep on decrement.
        
        for j in range(0, i + 1):        # val j to be run from 0 to i+1 val.
            
            if arr[j] > arr[j + 1]:      # If val of j > j+1 (its adjacent) val; then SWAP.
                
                arr[j], arr[j + 1] = arr[j + 1], arr[j]     # Swapping the vlaue in array.
                
                is_swap = True          # It says swapping is done, so TRUE.
        
        if is_swap == False: 
            
            # If no swapping is done, then return array as it is.
            return arr
        
    print(arr)
 

# Main/Driver code : 
arr = [5, 2, 6, 8, 1, 4, 9]

bubble_sort(arr)
                