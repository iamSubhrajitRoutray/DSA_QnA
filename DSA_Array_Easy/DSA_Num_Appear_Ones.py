'''Find the number that appears once, and the other numbers twice'''

''' BRUTE FORCE -> '''

# Function to check if the number in the array appear for only one time.
def single_element(arr):
    
    n = len(arr)
    
    # Check each element's count.
    for i in range(n):
        
        num = arr[i]
        count = 0
    
        # Count how many times does the num appears.
        for j in range(n):
       
            if arr[j] == num:
                count += 1
    
    # Return num if it appears once; which is the required answer.
    if count == 1:
        return num 
       
    return -1      # Fallback


# Driver code ->
array = [1, 2, 2, 1, 3]

result = single_element(array)

print(result)



''' OPTIMAL; USING XOR -> '''

def single_element(arr):
    
    xorr = 0
    
    for num in arr:
        
        xorr ^= num
    
    return xorr

array = [1, 2, 2, 1, 3]

result = single_element(array)

print(result)
