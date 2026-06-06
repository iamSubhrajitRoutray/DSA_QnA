'''Leaders in an Array'''


'''OPTIMAL APPROACH'''

def leader_array(arr):
    
    n = len(arr)
    
    ans = []
    
    leader = arr[-1]
    
    ans.append(leader)
    
    for i in range(n - 2, -1, -1):
    
        if arr[i] > arr[-1]:
            
            ans.append(arr[i])
    
    print(ans)


# Main/Driver code :  
array = [1, 8, 6, 4, 5]
leader_array(array)
            
            