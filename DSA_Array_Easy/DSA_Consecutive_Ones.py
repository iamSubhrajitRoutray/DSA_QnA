'''Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.'''


''' OPTIMAL APPRAOCH -> '''

def maximum_consecutive(arr):
    
    n = len(arr)
    
    count = 0
    
    max_one = 0
    
    for i in range(n):
    
        if arr[i] == 1:
            count += 1
    
        else:
            count = 0
        
        max_one = max(max_one, count)
    
    return max_one

array = [1, 2, 1, 1, 1, 3, 1, 1, 4]

res = maximum_consecutive(array)

print(f"The maximum consecutives 1's in the array is : {res}.")