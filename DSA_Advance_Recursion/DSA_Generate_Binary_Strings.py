'''Generate all binary strings without consecutive 1's
Q)
Given an integer n, the task is to generate all binary strings of size n without consecutive 1's.'''

# Examples: 

# Input : n = 4
# Output : 0000 0001 0010 0100 0101 1000 1001 1010

# Input : n = 3


def solve(index, flag, number, result):
    
    if index >= len(number):
        
        result.append("".join(number))
        
        return
    
    number[index] = "0"
    
    solve(index+1, True, number, result)
    
    if flag == True:
        
        number[index] = "1"
        
        solve(index+1, False, number, result)
        
        number[index] = "0"
        


def generate_binary_number(num):
    
    num_str = ["0"] * num
    
    res = []
    
    solve(0, True, num_str, res)
    
    return res



# MAIN/DRIVER CODE:

num_len = 3

answer = generate_binary_number(num_len)

print(f"\nBinary strings without consecutive 1's : {answer}\n")