'''Postfix to Prefix Conversion
# You are given a string s that represents the postfix form of a valid mathematical expression.
# Convert it to its prefix form.'''

# Examples :

# Input: s = "ab+"
# Output: "+ab"

# Explanation: In prefix form, operator comes before operands.
# Postfix to Infix: ab+ becomes a + b 
# Infix to Prefix: a + b becomes +ab 

# Input: s = "ab+c*"
# Output: "*+abc"

# Explanation:
# Postfix to Infix: ab+ becomes (a + b), then with c gives (a + b)*c
# Infix to Prefix: (a + b) becomes +ab, then with c gives *+abc

# Input: s = "ABC/-AK/L-*"
# Output: "*-A/BC-/AKL"

# Explanation: 
# Postfix to infix: ABC/-AK/L-* becomes (A - (B / C)) * ((A / K) - L)
# Convert left part to Prefix: (A - (B / C)) becomes -A/BC
# Convert right part to Prefix: ((A / K) - L) becomes -/AKL
# Combine both with * to get *-A/BC-/AKL



def convert(string):
    
    stack = []
    
    for char in string:
        
        if char.isalnum():
            
            stack.append(char)
        
        else:
            
            op1 = stack.pop()
            op2 = stack.pop()
            
            new_epxr = f"{char}{op2}{op1}"
            
            stack.append(new_epxr)
    
    return stack[-1]


# MAIN/DRIVER CODE:

string = "ab+c*"

answer = convert(string)

print(f"\nGiven String :- {string}\nConvert Postfix to Prefix gives :- {answer}\n")