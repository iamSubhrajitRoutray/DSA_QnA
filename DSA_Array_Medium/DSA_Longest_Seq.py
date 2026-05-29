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
        
    print(f'Longest consecutive sequence : {res} with lenght : {len(res)}')


'''Code Run -> '''
a = [0, 3, 7, 2, 5, 8, 4, 6, 1]

longest_sequence(a)