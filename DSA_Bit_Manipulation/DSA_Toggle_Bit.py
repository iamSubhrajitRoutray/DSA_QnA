'''Set the rightmost bit
Q)
Given a positive integer n, set the rightmost unset (0) bit of its binary representation to 1 and return the resulting integer.
If all bits are already set, return the number as it is.'''

class Toggle:

    def toggle_bit(self, num, i):
        
        new_num = (num ^ (1 << i))
        
        return new_num
    
    
    def binary(self, num):
        
        res = " "
        
        while num > 0:
            
            if num % 2 == 1:
                res += "1"
            else:
                res += "0"
            num //= 2
            
        res = res[::-1]
        
        return res
        


# MAIN/DRIVER CODE:
    
sol = Toggle()

number = 13
ith_bit = 1

binary_num = sol.binary(number)

print(f"\nBinary form of {number} = {binary_num}\n")

answer = sol.toggle_bit(number, ith_bit)

binary_ans = sol.binary(answer)

print(f"After unset of bit {ith_bit} : {binary_ans}= {answer}\n")
   