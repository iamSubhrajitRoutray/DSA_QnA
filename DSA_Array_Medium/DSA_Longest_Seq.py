'''Longest Consecutive Sequence in an Array
Return the length of the longest sequence of consecutive integers.
The integers in this sequence can appear in any order.'''


''' BRUTE FORCE -> '''

def longest_sequence(arr): 
    
    n = len(arr)
    
    longest = 0
    
    for i in range(n):
        
        num = arr[i]
        
        count = 1
        
        while num+1 in arr:
            
            count += 1
            
            num += 1
            
        longest = max(longest, count)
        
    return print(longest)
            
            
# Main Driver Code...
array = [1, 99, 101, 98, 2, 5, 3, 100, 1, 1]

longest_sequence(array)





''' BETTER APPROACH -> '''

def longest_sequence(arr):
    
    n = len(arr)
    
    arr.sort()
    
    last_smaller = float('inf')
    
    longest = 0
    
    count = 0
    
    for i in range(0, n):
        
        num = arr[i]
        
        if num - 1 == last_smaller:
            
            count += 1
           
            last_smaller = num
            
        elif num != last_smaller:
            
            count = 1
            
            last_smaller = num
        
        longest = max(longest, count)
        
    print(count)


# Main Driver Code...
array = [1, 99, 101, 98, 2, 5, 3, 100, 1, 1]
longest_sequence(array)





''' OPTIMAL APPROACH -> '''

def longest_sequence(arr):
    
    n = len(arr) 
    
    my_set = set()
    
    for i in range(0, n):
        
        my_set.add(arr[i])
    
    longest = 0
    
    for num in my_set:
        
        if num - 1 not in my_set:
           
            x = num
            
            count = 1
        
        if x + 1 in my_set:
            
            count += 1
           
            x += 1
        
        longest = max(longest,count)
    
    print(longest)


# Main Driver Code...
array = [1, 99, 101, 98, 2, 5, 3, 100, 1, 1]
longest_sequence(array)