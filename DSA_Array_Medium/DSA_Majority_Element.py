'''Find the highest/lowest frequency element'''

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
    print(f'The element "{max_ele}" having maximum no. of occurence.')
    print(f'It occurs {max_freq} times in the given array.')
    
    

# Main/Driver code
arr = [1,3,1,15,3,1,5,1]

# Function call
majority(arr)



