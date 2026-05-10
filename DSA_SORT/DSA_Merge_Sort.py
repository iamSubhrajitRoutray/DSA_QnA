def merge_sort(arr):
    
    num = len(arr)
    
    if num <= 1:
        return arr
    
    mid = num // 2
    
    left_half = arr[: mid]
    right_half = arr[mid :]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge_array(left_half,right_half)




def merge_array(left,right):
    
    result = []
    
    i = 0
    j = 0
    
    n = len(left)
    m = len(right)
    
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
            
        else:
            result.append(right[j])
            j += 1
            
    if i < n:
        while i < n:
            result.append(left[i])
            i += 1
            
    if j < m:
        while j < m:
            result.append(right[j])
            j += 1
    
    return result



# DRIVER CODE ->

array = [4,6,2,9,7,1,5,8]

merge_sort(array)

print(f'Sorted array :- {array}')