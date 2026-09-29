'''Subset Sum
Q)
Given an array arr of integers, return the sums of all subsets in the list.  Return the sums in any order.'''



# Examples:

# Input: arr[] = [2, 3]
# Output: [0, 2, 3, 5]
# Explanation: When no elements are taken then Sum = 0. When only 2 is taken then Sum = 2.
# When only 3 is taken then Sum = 3. When elements 2 and 3 are taken then Sum = 2+3 = 5.


# Input: arr[] = [1, 2, 1]
# Output: [0, 1, 1, 2, 2, 3, 3, 4]
# Explanation: The possible subset sums are 0 (no elements), 1 (either of the 1's), 2 (the element 2), and their combinations.


# Input: arr[] = [5, 6, 7]
# Output: [0, 5, 6, 7, 11, 12, 13, 18]
# Explanation: The possible subset sums are 0 (no elements), 5, 6, 7, and their combinations.




def backtrack(index, total, subset, nums):
    
    if index >= len(nums):
        subset.append(total)
        return
    
    summ = total + nums[index]
    
    backtrack(index + 1, summ, subset, nums)
    
    summ = total
    
    backtrack(index + 1, summ, subset, nums)
    
    

def sum_of_subsets(array):
    
    res = []
    
    backtrack(0, 0, res, array)
    
    res.sort()
    
    return res



# MAIN/DRIVER CODE:

array = [2, 3]

answer = sum_of_subsets(array)

print(f"\nSums of all subsets : {answer}\n")
    