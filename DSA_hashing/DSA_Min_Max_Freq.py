'''Q) Find the highest/lowest frequency element'''


def frequency(arr, num):
   
    # Track if an element has already been counted
    visted = [False] * num
   
    # Store max frequency seen so far
    max_freq = 0
   
    # Store min frequency (start high)
    min_freq = num
   
    # Element with max frequency
    max_ele = 0
   
    # Element with min frequency
    min_ele = 0
    
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
            
        # Update the min frequency   
        if count < min_freq:
        
            min_ele = arr[i]
        
            min_freq = count
            
        # Print all the elemnets with their respective frequency
        print(f'{arr[i]} : {count}')
        
    # Print the max and min element
    print(f'Element with maximum freq : {max_ele} with {max_freq} no. of occurence')
    
    print(f'Element with minimum freq : {min_ele} with {min_freq} no. of occurence')
    

# Main/Driver code : 
arr = [1, 3, 1, 15, 3, 1, 5, 1]

n = len(arr)

frequency(arr, n)
            