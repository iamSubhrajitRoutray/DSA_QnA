'''Q) Given an array of N integers, write a program to implement the Selection Sort Algorithm.'''



'''SELECTION SORT in ascending order'''

def selection_sort(arr):
    
    num = len(arr)
    
    for i in range(num):
        
        min_index = i
    
        for j in range(i + 1, num):
            
            if arr[j] < arr[min_index]:
                
                min_index = j
    
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    print(arr)
    

# Main/Driver code :

array = [13,46,24,52,20,9]

print('Sorted array : ')

selection_sort(array)



'''SELECTION SORT in descending order'''

def selection_sort(arr):
    
    num = len(arr)
    
    max_ind = num-1
    
    for i in range(num):
        
        if arr[max_ind] > arr[i]:
        
            max_ind = i
    
        for j in range(i, num):
        
            if arr[j] > arr[max_ind]:
        
                max_ind = j
    
        arr[i],arr[max_ind] = arr[max_ind],arr[i]
    
    print(arr)
    
    
# Main/Driver code ->
array = [30, 9, 5, 10, 4, 1]

selection_sort(array) 