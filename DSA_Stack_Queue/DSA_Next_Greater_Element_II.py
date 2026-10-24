'''# Next Greater Element II

Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]),
return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array,
which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.'''

# Example 1:

# Input: nums = [1,2,1]
# Output: [2,-1,2]

# Explanation:
# The first 1's next greater number is 2;
# The number 2 can't find next greater number. 
# The second 1's next greater number needs to search circularly, which is also 2.

# Example 2:

# Input: nums = [1,2,3,4,3]
# Output: [2,3,4,-1,4]



'''OPTIMAL APPROACH'''



def next_greater(array):
    
    num = len(array)
    
    result = [-1] * num
    
    stack = []
    
    for i in range((2 * num - 1), -1, -1):
        
        while stack and stack[-1] <= array[i % num]:
            
            stack.pop()
        
        if i < num:
            
            if stack:
                
                result[i] = stack[-1]
        
        stack.append(array[i % num])
    
    return result


        
# MAIN/DRIVER CODE: 
        
array = [1, 2, 3, 4, 3]

print(f"\nGiven array: {array}\n")

answer = next_greater(array)

print(f"Array of Next greater element: {answer}\n")
    
    
    
    