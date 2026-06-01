'''Count frequency of each element in the array'''

# defining the function

def frequency(arr, num):
    
    visited = [False] * num     # making an array to keep in check if we've visited that num/index
    
    for i in range(num):
    
        if visited[i]:     # continue if True 
            continue
        
        count = 1      # initiliazing the counter to 1
    
        for j in range(i + 1, num):       # j will loop from i+1 to avoid repeatation of indexes
    
            if arr[i] == arr[j]:
    
                visited[j] = True      # will increment by 1 if we find the same num in the given array
                count += 1
                
        print(f'{arr[i]} : {count}')
        

arr = [5,10,100,15,10,50,5,15]

num = len(arr)

frequency(arr, num)