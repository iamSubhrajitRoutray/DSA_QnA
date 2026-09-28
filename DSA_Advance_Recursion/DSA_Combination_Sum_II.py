'''Combination Sum II
Q)
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.'''

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]


# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]



'''BRUTE-FORCE APPROACH'''


def backtrack(index, total, subset, result, nums, target):
    
    if total == target:
        result.add(tuple(subset.copy()))
        return
    
    if total > target:
        return
    
    if index >= len(nums):
        return
    
    summ = total + nums[index]
    
    subset.append(nums[index])
    
    backtrack(index+1, summ, subset, result, nums, target)
    
    summ = total
    
    subset.pop()
    
    backtrack(index+1, summ, subset, result, nums, target)
    
    

def combinations(candidates, target):
    
    candidates.sort()
    
    result = set()
    
    backtrack(0, 0, [], result, candidates, target)
    
    return result



# MAIN/DRIVER CODE:

candidates = [10, 1, 2, 7, 6, 1, 5]

target = 8

answer = combinations(candidates, target)

print(f"\nAll unique combinations of candidates having sum {target} : {answer}\n")







'''OPTIMAL APPROACH'''


def backtrack(index, target, subset, result, nums):
    
    if target == 0:
        result.add(tuple(subset.copy()))
        return
    
    if target < 0:
        return
    
    if index >= len(nums):
        return
   
    for i in range(index, len(nums)):
        
        if i > index and nums[i] == nums[i - 1]:
            continue
        
        if nums[i] > target:
            break
        
        subset.append(nums[i])
        
        backtrack(i + 1, target - nums[i], subset, result, nums)
        
        subset.pop()
        
    
    
    
def combination_solution(candidates, target):
    
    candidates.sort()
    
    result = set()
        
    backtrack(0, target, [], result, candidates)
    
    return result



# MAIN/DRIVER CODE:

candidates = [10, 1, 2, 7, 6, 1, 5]

target = 8

answer = combination_solution(candidates, target)

print(f"\nAll unique combinations of candidates having sum {target} : {answer}\n")
