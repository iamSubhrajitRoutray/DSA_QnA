'''Q) Given an array of n integers, sort the array using the Quicksort method.'''

# Function for parition in the given array using pivot element
def partition(arr, low, high):
    
    pivot = arr[low]
    
    i = low
    
    j = high
    
    while i < j:
       
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        
        while arr[j] > pivot and j >= low + 1:
            j -= 1
    
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[low], arr[j] = arr[j], arr[low]
    
    return j


# Function for Quick Sort Algorithm 
def quick_sort(arr, low, high):
    
    if low < high:
        
        pivot_index = partition(arr, low, high)
        
        quick_sort(arr, low, pivot_index - 1)
        
        quick_sort(arr, pivot_index + 1, high)
        
        
# Main/Driver code : 
array = [4, 9, 5, 2, 7, 3, 6, 8, 1]

num = len(array)

quick_sort(array, 0, num-1)

print(f'Sorted array : {array}')
    
    