'''Max Consecutive Ones III

Given a binary array nums and an integer k,
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.'''

 
# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6

# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10

# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.




'''BRUTE FORCE APPROACH'''


def max_ones(arr, k):
    
    max_i = 0
    
    
    
    for i in range(len(arr)):
        
        zeros = 0
        
        for j in range(i, len(arr)):
            
            if arr[j] == 0:
                
                zeros += 1
            
            if zeros > k:
                break
            
            max_i = max(max_i, (j - i + 1))
            
    return max_i


# MAIN/DRIVER CODE: 

nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

ans = max_ones(nums, k)

print(ans)


# TIME COMPLEXITY : O(N^2)
# SPACE COMPLEXITY : O(1)


'''BETTER APPROACH'''


def consec_max_one(arr, k):
    
    max_num_1 = 0
    
    zeros = 0
    
    left, right = 0, 0
    
    while (right < len(arr)):
        
        if (arr[right] == 0):
            
            zeros += 1
            
        while (zeros > k):
            
            if arr[left] == 0:
                
                zeros -= 1

            left += 1
        
        if (zeros <= k):
            
            max_num_1 = max(max_num_1, (right - left + 1))
        
        right += 1
    
    return max_num_1


# MAIN/DRIVER CODE: 

nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

ans = consec_max_one(nums, k)

print(ans)


# TIME COMPLEXITY : O(N) + O(N)
# SPACE COMPLEXITY : O(1)




'''OPTIMAL APPROACH'''

def get_max_one(array, k):
    
    zeros = 0
    
    left, right = 0, 0
    
    max_1 = 0
    
    while right < len(array):
        
        if array[right] == 0:
            
            zeros += 1
            
        if zeros > k:
            
            if array[left] == 0:
                
                zeros -= 1
        
            left += 1
        
        if zeros <= k:
            
            max_1 = max(max_1, (right - left + 1))
        
        right += 1
    
    return max_1



# MAIN/DRIVER CODE: 

nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

ans = get_max_one(nums, k)

print(ans)



# TIME COMPLEXITY :O(N)
# SPACE COMPLEXITY : O(1)
    