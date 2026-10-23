'''Infix to Prefix'''



def priority(char):
    
    if char == "^":
        return 3
    
    if char == "*" or char == "/":
        return 2
    
    if char == "+" or char == "-":
        return 1
    
    return 0



def convert_infix_to_prefix(string):
    
    string = string[::-1]
    
    string = string.replace("(", "temp").replace(")", "(").replace("temp", ")")
    
    stack = []
    
    result = []
    
    for char in string:
        
        if ("a" <= char <= "z") or ("A" <= char <= "Z") or ("0" <= char <= "9"):
        
            result.append(char)    
            
        elif char == "(":
        
            stack.append(char)
        
        elif char == ")":
            
            while stack and stack[-1] != "(":
            
                result.append(stack.pop())
            
            stack.pop()
        
        else:
            
            while stack and priority(stack[-1]) > priority(char):
                
                result.append(stack.pop())
            
            stack.append(char)
            
        
    while stack:
        
        result.append(stack.pop())
    
    return "".join(result[::-1])
        


# MAIN/DRIVER CODE:

given_string = "(A+B)*C-D+F"

answer = convert_infix_to_prefix(given_string)

print(f"\nConverting {given_string} from infix to prefix gives : {answer}\n")


                