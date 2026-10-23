'''Infix to Postfix

You are given a string s representing an infix expression. Convert this infix expression to a postfix expression.

Infix expression: The expression of the form a op b. When an operator is in between every pair of operands.
Postfix expression: The expression of the form a b op. When an operator is followed for every pair of operands.
Note: The precedence order is as follows: (^) has the highest precedence and is evaluated from right to left,
(* and /) come next with left to right associativity, and (+ and -) have the lowest precedence with left to right associativity'''

# Examples :

# Input: s = "a*(b+c)/d"
# Output: abc+*d/

# Explanation: The expression is a*(b+c)/d. First, inside the brackets, b+c becomes bc+. Now the expression looks like a*(bc+)/d. Next, multiply a with (bc+), so it becomes abc+* . Finally, divide this result by d, so it becomes abc+*d/.


# Input: s = "a+b*c+d"
# Output: abc*+d+

# Explanation: The expression a+b*c+d is converted by first doing b*c -> bc*, then adding a -> abc*+, and finally adding d -> abc*+d+.


# Input: s = "(a+b)*(c+d)"
# Output: ab+cd+*

# Explanation: The expression (a+b)*(c+d) is converted by first doing (a+b) -> ab+, then doing (c+d) -> cd+, and finally the expression ab+*cd+ becomes ab+cd+*


def priority(char):
    
    if char == "^":
        return 3
    
    if char == "*" or char == "/":
        return 2
    
    if char == "+" or char == "-":
        return 1
    
    return 0



def convert_infix_to_postfix(string):
    
    stack = []
    
    result = []
    
    for char in string:
        
        if ("a" <= char <= "z") or ("A" <= char <= "Z") or ("0" <= char <= "9"):
            
            result.append(char)
            
        # if char is "(" push it in the stack
            
        elif char == "(":
            
            stack.append(char)
        
        # if char is ")", keep char popping from the stack and appending in the result until ")" meets "(":
           
        elif char == ")":
            
            while stack and stack[-1] != "(":
                
                result.append(stack.pop())
            
            stack.pop()
    
        # if char is an operator:        

        else:
            
            while stack and priority(stack[-1]) >= priority(char):
                
                result.append(stack.pop())
            
            stack.append(char)
    
    # Pop remaining char from the stack:
    
    while stack:
        
        result.append(stack.pop())
    
    return "".join(result)




# MAIN/DRIVER CODE:

given = "a+b*(c^d-e)"

answer = convert_infix_to_postfix(given)

print(f"\nConverting {given} from infix to postfix gives : {answer}\n")