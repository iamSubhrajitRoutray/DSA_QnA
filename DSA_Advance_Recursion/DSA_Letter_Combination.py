'''Letter Combinations of a Phone Number
Q)
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.'''


# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


# Example 2:

# Input: digits = "2"
# Output: ["a","b","c"]





numpad = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}




def backtrack(index, digits, subset, result):
    
    if index >= len(digits):
        result.append("".join(subset.copy()))
        return
    
    for char in numpad[digits[index]]:
       
        subset.append(char)
        
        backtrack(index + 1, digits, subset, result)
        
        subset.pop()
        
        
        
def combination(digits):
    
    result = []
    
    backtrack(0, digits, [], result)
    
    return result



#  MAIN/DRIVER CODE:

digits = "23"

answer = combination(digits)

print(f"\n{answer}\n")

