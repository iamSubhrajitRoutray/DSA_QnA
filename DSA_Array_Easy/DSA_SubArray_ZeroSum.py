'''Q) Lenght of Longest SubArray with given Zero Sum'''


''' BRUTE FORCE APPROACH -> '''

def sub_array(arr):
    
    n = len(arr)
    
    max_len = 0
    
    for i in range(0, n):
        
        total = 0
        
        for j in range(i, n):
            
            total = total + arr[j]
            
            if total == 0:
                max_len = max(max_len, j - i + 1)
                
    print(max_len)
    
    
# Main/Driver code :  
array = [6, -2, 2, -8, 1, 7, 4, -10]

sub_array(array)



'''OPTIMAL APPROACH ->'''

def sub_array(arr):
    
    n = len(arr)
    
    hash_map = {}
    
    k = 0
    
    max_len = 0
    
    for i in range(n):
        
        k = k + arr[i]
        
        if k == 0: 
           
            max_len = i + 1
        
        if k in hash_map:
            
            max_len = max(max_len, i - hash_map[k])
            
        else:
            hash_map[k] = i
            
    print(max_len)
    

# Main/Driver code :  
array = [9, -3, 3, -1, 6, -5]

sub_array(array)
            
            
    
    