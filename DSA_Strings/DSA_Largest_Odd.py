'''Largest Odd Number in a String
Q)
Given a string s, representing a large integer, the task is to return the largest-valued odd integer (as a string) that is a substring of the given string s.
The number returned should not have leading zero's.
But the given input string may have leading zero'''



def find_largest(s):
    
    n = len(s)
    
    
    for i in range(n-1, -1, -1):
        
        if int(s[i]) % 2 == 1:
            
            if int(s[0]) == 0:
            
                return s[1 : i + 1]
            else:
                return s[0 : i + 1]
    
    return ""


# Main/Driver code :

s = "0214638"

print(f"Given string :{s}")

answer = find_largest(s)

print(f"largest odd number in given string : {answer}")
        