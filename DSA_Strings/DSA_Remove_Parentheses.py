'''Remove Outermost Parentheses
Q)
A valid parentheses string is defined by the following rules:

It is the empty string " ".
If A is a valid parentheses string, then so is "(" + A + ")".
If A and B are valid parentheses strings, then A + B is also valid.

A primitive valid parentheses string is a non-empty valid string that cannot be split into two or more non-empty valid parentheses strings.

Given a valid parentheses string s,
your task is to remove the outermost parentheses from every primitive component of s and return the resulting string.'''



def removal(s):
    
    counter = 0
    
    result = ""
    
    for char in s:
        
        if char == "(":
            counter += 1
            
            if counter > 1:
              result += char
              
        else:            
            counter -= 1
            
            if counter > 0:
                result += char

    return result



# Main/Driver code:

string = "()(()())(())"

ans = removal(string)

print(ans)
        