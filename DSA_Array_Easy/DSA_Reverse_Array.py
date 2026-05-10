'''Reverse a given array in the without changing the serial of the elements.'''

def reverse(arr, n):
    
    n = len(arr)
    
    left = 0
    right = n - 1
    
    for _ in range(n):
    
        if left < right:
            
            arr[left], arr[right] = arr[right], arr[left]
            
            left += 1
            right -= 1
    
    print(arr)
    

array = [1,2,3,4,5,6,7]

l = len(array)

reverse(array, l)