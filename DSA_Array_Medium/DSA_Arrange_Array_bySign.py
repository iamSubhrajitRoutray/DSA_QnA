'''Rearrange Array Elements by Sign
Q) There is an array "arr" of size "n/l" with an equal number of positive and negative elements.
Without altering the relative order of positive and negative elements,
you must return an array of alternately positive and negative values.'''



'''BRUTE FORCE APPROACH ->'''

def re_arrange(arr):
    
    n = len(arr)
    
    pos = []
    
    neg = []
    
    for i in range(n):
        
        if arr[i] > 0:
            pos.append(arr[i])
        
        else:
            neg.append(arr[i])
        
        
    for i in range(n // 2):
        
        arr[2 * i] = pos[i]
        
        arr[2 * i + 1] = neg[i]
    
    print(arr)


# Main/Driver code :  
array = [1, 2, -3, -1, 4]

re_arrange(array)



'''OPTIMAL APPROACH'''

def re_arrange(arr):
    
    l = len(arr)
    
    ans = [0] * l
    
    neg_index = 1
    
    pos_index = 0
    
    for i in range(l):
    
        if arr[i] < 0:
    
            ans[neg_index] = arr[i]
            neg_index += 2
        
        if arr[i] > 0:
    
            ans[pos_index] = arr[i]
            pos_index += 2
    
    print(ans)
    

# Main/Driver code :  
array = [1, 2, -3, -1, 4]

re_arrange(array)