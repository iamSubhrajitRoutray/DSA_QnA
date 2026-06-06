'''Union of Two Sorted Arrays
Q) Given two sorted arrays, arr1, and arr2 of size n and m.
Find the union of two sorted arrays.'''

# The union of two arrays can be defined as the common and distinct elements in the two arrays.



'''OPTIMAL APPRAOCH->'''

def union(arr1, arr2):
    
    arr_set = set(arr1) | set(arr2)
    
    return sorted(arr_set)


# Main/Driver code :  
array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(array1)

array2 = [2, 3, 4, 4, 5, 11, 12]
print(array2)

array_union = union(array1,array2)

print(f'Union of arrays : {array_union}')  






''' BRUTE FORCE APPROACH -> '''

def union(arr1, arr2):
    
    n = len(arr1)
    m = len(arr2)
    
    i = 0
    j = 0
    
    result = []
    
    while i < n and j < m:
        
        if arr1[i] <= arr2[j]:
        
            if len(result) == 0 or result[-1] != arr1[i]:
        
                result.append(arr1[i])
            
            i += 1
        
        else:
        
            if len(result) == 0 or result[-1] != arr2[j]:
        
                result.append(arr2[j])
            
            j += 1
        
   
    while i < n:
        
        if len(result) == 0 or result[-1] != arr1[i]:
        
            result.append(arr1[i])
        
        i += 1
    
    
    while j < m:
    
        if len(result) == 0 or result[-1] != arr2[j]:
        
            result.append(arr2[j])
        
        j += 1
    
    return result


# Main/Driver code :  
array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(array1)

array2 = [2, 3, 4, 4, 5, 11, 12]
print(array2)

array_union = union(array1,array2)

print(f'Union of arrays : {array_union}') 