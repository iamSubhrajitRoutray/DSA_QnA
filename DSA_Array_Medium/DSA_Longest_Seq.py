'''Longest Consecutive Sequence in an Array'''

def longest_sequence(arr):
    
    res = []
    
    n = len(arr)
    
    arr.sort()
    
    i = 0
    
    res.append(arr[i])
    
    for i in range(n):
        
        for j in range(i + 1, n):
            
            if arr[j] == arr[i] + 1:
                
                res.append(arr[j])
        
    print(f'{res}')


'''Code Run -> '''
a = [100, 2, 200, 3, 1, 4]

longest_sequence(a)