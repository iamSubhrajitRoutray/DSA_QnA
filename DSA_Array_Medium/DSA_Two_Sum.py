'''Two Sum : Check if a pair with given sum exists in Array.'''

def array_sum(arr, target):
    
    n = len(arr)
       
    for i in range(n - 1):
        
        for j in range(i + 1, n): 
            
            if arr[i] + arr[j] == target:
                
                return print('YES')
    
    return print('NO')


def sum_pair(arr, target):
   
    n = len(arr)
    
    for i in range(n - 1):
         
        for j in range(i + 1, n):
            
            if arr[i] + arr[j] == target:
                
                return print([i, j])
            
    return print([-1,-1])
                


arr = [1,2,3,4,5]

target = 9

array_sum(arr, target)

sum_pair(arr, target)





'''OPTIMAL APPROACH'''

# def array_sum(arr,target):
    
#     l = len(arr)
    
#     hash_map = {}
    
#     for i in range(l):
        
#         remaining = target-arr[i]
        
#         if remaining in hash_map:
        
#             print([hash_map[remaining],i])

#         hash_map[arr[i]] = i



# arr = [1,2,3,4,5]

# target = 9

# array_sum(arr, target)
        
    
    