'''Valid Parentheses
Q)

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.'''
 

# Example 1:

# Input: s = "()"
# Output: true


# Example 2:

# Input: s = "()[]{}"
# Output: true


# Example 3:

# Input: s = "(]"
# Output: false


# Example 4:

# Input: s = "([])"
# Output: true


# Example 5:

# Input: s = "([)]"
# Output: false





def check_if_valid(string):
    
    stack = []
    
    for brackets in string:
        
        if (
            (brackets == "(") or
            (brackets == "[") or
            (brackets == "{")
        ):
            
            stack.append(brackets)
        
        else:
            
            if len(stack) == 0:
            
                return False
            
            e = stack.pop()
            
            if (
                (brackets == ")" and e == "(") or
                (brackets == "]" and e == "[") or
                (brackets == "}" and e == "{")
            ):
                continue
            
            else:
                
                return False
    
    return len(stack) == 0


# MAIN/DROVER CODE:


string = "({[]}){}[()]"

answer = check_if_valid(string)

print(f"\n{answer}\n")


