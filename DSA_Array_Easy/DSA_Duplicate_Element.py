'''Given an integer array sorted in non-decreasing order,
remove the duplicates in place such that each unique element appears only once.
If there are k elements after removing the duplicates,
then the first k elements of the array should hold the final result.
It does not matter what you leave beyond the first k elements.'''



''' BRUTE FORCE APPROACH -> '''

def remove_duplicate(arr):
    
    n = len(arr)
    
    freq_list = {}
    
    for i in range(n):
    
        freq_list[arr[i]] = 0
        
    j = 0
    
    for key in freq_list:
        
        arr[j] = key
        
        j += 1
    
    return print(f'The final number of elements in the array is : {j}.')

array = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4]

remove_duplicate(array)





''' OPTIMAL APPROACH -> '''

def duplicate(arr):
    
    n = len(arr)
    
    i = 0
    j = i + 1
    
    if n == 1:
        return 1
    
    while j < n:
        
        if arr[j] != arr[i]:
            
            i += 1
            
            arr[i], arr[j] = arr[j], arr[i]
        
        j += 1
    
    return print(f'The final no. of elements in the array is : {i + 1}')
    
    

array = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4]

duplicate(array)

