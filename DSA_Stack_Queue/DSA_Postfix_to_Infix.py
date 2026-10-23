'''Postfix to Infix Conversion

# Given a string s that represents the postfix form of a valid mathematical expression.
# Convert it to its infix form.'''

# Example:

# Input: s = "ab*c+" 
# Output: ((a*b)+c)

# Explanation: The postfix expression ab*c+ represents (a*b)+c.
# Therefore, its equivalent infix expression is ((a*b)+c).

# Input: s = "abc/-"
# Output: (a-(b/c))

# Explanation: The postfix expression abc/- represents a-(b/c).
# Therefore, its equivalent infix expression is (a-(b/c)).


def convert(string):
    
    stack = []
    
    for char in string:
        
        if char.isalnum():
        
            stack.append(char)
        
        else:
            
            operand1 = stack.pop()
            operand2 = stack.pop()
            
            new_expression = f"({operand2}{char}{operand1})"
            
            stack.append(new_expression)
    
    return stack[-1]



# MAIN/DRIVER CODE:

string = "ab*c+"

answer = convert(string)

print(f"\nGiven String :- {string}\nConvert Postfix to Infix gives :- {answer}\n")