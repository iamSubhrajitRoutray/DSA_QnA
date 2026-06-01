'''Given an array, find the second smallest and second largest element in the array.'''



''' DIRECT APPROACH -> '''

array = [3,1,6,4,9,5,10,7,2,8]

array.sort()

print(f'The sorted array is : {array}')

ele = len(array) - 1

print(f'The second largest element in the array is : {ele}')





''' BRUTE FORCE APPROACH -> '''

def second_largest(arr):
    
    n = len(arr)
    
    for i in range(1, n):
        
        key = arr[i]
        
        j = i - 1
        
        while j >= 0 and arr[j] > key:
        
            arr[j + 1] = arr[j]
        
            j -= 1
        
        arr[j + 1] = key
    
    print(arr)
    

array = [3, 1, 6, 4, 9, 5, 10, 7, 2, 8]

print(f'The given array :')

second_largest(array)

ele = array[len(array) - 2]

print(f'second largest element in the array : {ele}')






''' OPTIMAL APPROACH -> ''' 

from math import inf


def second_largest(arr):
    
    largest = float(-inf)
    
    second_largest = float(inf)
    
    n = len(arr)
    
    for i in range(n):
       
        if arr[i] > largest:
          
            second_largest = largest
          
            largest = arr[i]
       
        elif arr[i] > second_largest and arr[i] != largest:
       
            second_largest = arr[i]
    
    return second_largest



array = [3, 1, 6, 4, 9, 5, 10, 7, 2, 8]

print('The given array is :- ',array)

ele = second_largest(array)

print(f'The second alrgest element in the array is : {ele}')





''' DIRECT APPROACH -> '''

array = [3,1,6,4,9,5,10,7,2,8]

array.sort()

print(f'The sorted array is : {array}')

ele = len(array) - 1

print(f'The second largest element in the array is : {ele}')
