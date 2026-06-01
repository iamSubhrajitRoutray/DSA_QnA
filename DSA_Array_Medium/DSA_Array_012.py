'''Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order.
The sorting must be done in-place,
without making a copy of the original array.'''



''' BRUTE FORCE APPROACH-> '''

def function(arr):
    
    count0 = count1 = count2 = 0
    
    for num in arr:
    
        if num == 0:
            count0 += 1
    
        if num == 1:
            count1 += 1
    
        if num == 2:
            count2 += 1
    
        index = 0
    
    for _ in range(count0):
    
        arr[index] = 0
        index += 1
    
    for _ in range(count1):
    
        arr[index] = 1
        index += 1
    
    for _ in range(count2):
    
        arr[index] = 2
        index += 1
    
    return print(arr)


arr = [1,0,1,1,0,2,0,2,1,2,0]
function(arr)
    
 
 
''' BETTER APPROACH -> '''
   
def function(arr):
    
    l = len(arr)
    
    count0 = count1 = count2 = 0
    
    for num in arr:
        
        if num == 0:
            count0 += 1
        
        if num == 1:
            count1 += 1
        
        if num == 2:
            count2 += 1
    
    for i in range(0, count0):
        arr[i] = 0
    
    for i in range(count0, count0 + count1):
        arr[i] = 1
    
    for i in range(count0 + count1, l):
        arr[i] = 2
        
    return print(arr)


array = [1,0,1,1,0,2,0,2,1,2,0]
function(array)
        
            
        