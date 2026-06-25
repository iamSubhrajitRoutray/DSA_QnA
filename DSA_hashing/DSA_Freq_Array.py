'''Q) Count frequency of each element in the array'''



def frequency(arr, num):
    
    visited = [False] * num     # Making an array to keep in check if we've visited that num/index
    
    for i in range(num):
    
        if visited[i]:     # Continue if True 
            continue
        
        count = 1      # Initiliazing the counter to 1
    
        for j in range(i + 1, num):       # j will loop from i+1 to avoid repeatation of indexes
    
            if arr[i] == arr[j]:
    
                visited[j] = True      # Will increment by 1 if we find the same num in the given array
                count += 1
                
        print(f'{arr[i]} : {count}')
        
        
# Main/Driver code : 

arr = [5, 10, 100, 15, 10, 50, 5, 15]

num = len(arr)

frequency(arr, num)