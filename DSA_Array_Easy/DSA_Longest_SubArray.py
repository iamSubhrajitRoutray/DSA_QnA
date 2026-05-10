'''Longest SubArray with given Sum K(Positives)'''

def sub_array(arr, k):
    
    n = len(arr)
    
    max_len = 0
    
    for i in range(0, n):
        
        total = 0
        
        for j in range(i, n):
            
            total = total + arr[j]
            
            if total == k:
                max_len = max(max_len, j - i + 1)
                
    print(max_len)
    


array = [10, 5, 2, 7, 1, 9]

k = 15
 
sub_array(array, k)