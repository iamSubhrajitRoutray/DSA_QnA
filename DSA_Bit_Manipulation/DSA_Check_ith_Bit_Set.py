'''Check if the i-th bit is set or not
Q)
Given two integers n and i, return true if the ith bit in the binary representation of n
(counting from the least significant bit, 0-indexed) is set (i.e., equal to 1).
Otherwise, return false.'''




'''BY USING LEFT SHIFT'''


def check_bit_set(num, i):
    
    if ((num & (1 << i)) != 0):
    
        return True
    
    else:
    
        return False
   
   
    
# MAIN/DRIVER CODE:
  
number = 13
ith_bit = 2

answer = check_bit_set(number, ith_bit)

print(f"\n{answer}\n")




'''BY USING RIGHT SHIFT'''


def check_bit_set(num, i):
    
    if (((num >> i) & 1) != 0):
        return True
    else:
        return False


    
# MAIN/DRIVER CODE:
  
number = 13
ith_bit = 2

answer = check_bit_set(number, ith_bit)

print(f"{answer}\n")

