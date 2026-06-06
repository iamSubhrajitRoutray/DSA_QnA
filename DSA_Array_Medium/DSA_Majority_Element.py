'''Q) Find the Majority Element that occurs more than N/2 times'''


def majority(arr):
    
    num = len(arr)
   
    # Track if an element has already been counted
    visted = [False] * num
   
    # Store max frequency seen so far
    max_freq = 0
   
    # Store min frequency (start high)
    
   
    # Element with max frequency
    max_ele = 0
   
    # Element with min frequency
    
    for i in range(num):
        
        # Skip already processed elements
        if visted[i]:
            continue
        
        # Count frequency of arr[i]
        count = 1
        
        for j in range(i + 1, num):
            if arr[i] == arr[j]:
                
                # Mark as visited
                visted[j] = True
                
                # increment the counter
                count += 1
        
        # Update the max frequency
        if count > max_freq:
            
            max_ele = arr[i]
            
            max_freq = count
        
    # print the max and min element
    print(f'Element with maximum no. of occurence : {max_ele}')
    
    print(f'Frequency of element : {max_freq}')
    
    

# Main/Driver code :  
arr = [1, 3, 1, 15, 3, 1, 5, 1]

majority(arr)



