
'''Remove the last set bit of the given number.'''


class Removal:
        
    def set_removal(self, num):
        
        new_num = (num & (num - 1))
        
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
    
sol = Removal()

number = 15
binary_num = sol.binary(number)

print(f"\nBinary form of {number} = {binary_num}\n")

answer = sol.set_removal(number)

binary_ans = sol.binary(answer)

print(f"After removal of set bit : {binary_ans}= {answer}\n")
   