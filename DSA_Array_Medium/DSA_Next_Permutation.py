'''Q) Next Permutation : find next lexicographically greater permutation'''


''' OPTIMAL APPROACH '''

def next_permutation(arr):
    
    n = len(arr)
    
    index = -1
    
    for i in range(n - 2, -1, -1):
        
        if arr[i] < arr[i + 1]:
            
            index = i
            break
        
    
    if index == -1:
        
        arr.reverse()
        return
    
    
    for i in range(n - 1, index, -1):
        
        if arr[i] > arr[index]:
            
            arr[i], arr[index] = arr[index], arr[i]
            break
        
    
    arr[index + 1: ] = reversed(arr[index + 1: ])
    

# Main/Driver code : 
def run_code():
    
    array = [1,2,3]
    
    next_permutation(array)
    
    print(''.join(map(str,array)))

run_code()


