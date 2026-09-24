'''
Q)
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.'''


# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]


# Example 2:
# Input: n = 1
# Output: ["()"]



def solve(index, total, brackets, result):
    
    if (index >= len(brackets)):
        
        if total == 0:
            result.append("".join(brackets))
        return
    
    if (total > (len(brackets) // 2)):
        return
    
    if (total < 0):
        return
    
    brackets[index] = "("
    
    Sum = total + 1
    
    solve(index + 1, Sum, brackets, result)
    
    brackets[index] = ")"
    
    Sum = total - 1
    
    solve(index + 1, Sum, brackets, result)
    



def generate(num):
    
    brackets = [""] * (num * 2)
    
    res = []
    
    solve(0, 0, brackets, res)
    
    return res



# MAIN/DRIVER CODE:


number = 2

answer = generate(number)

print(f"\nAll well-formed parentheses : {answer}\n")

