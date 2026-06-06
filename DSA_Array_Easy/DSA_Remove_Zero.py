'''Q) Move all Zeros to the end of the array'''


def removal(arr):
    
    n = len(arr)
    
    for i in range(0, n):
        
        if arr[i] == 0:
    
            e = arr.pop(i)
    
            arr.insert(n - 1, e)
    
    print(arr)
    
# Main/Driver code : 
array = [1, 2, 0, 1, 0, 4, 0]
removal(array)
    