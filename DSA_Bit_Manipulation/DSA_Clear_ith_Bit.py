'''Clear the i-th bit'''

# It measn if the i-th bit is 1, toggle it to 0.

class Clearance:
    
    def clear_bit(self, num, i):
        
        new_num = num & (~(1 << i))
        
        return new_num
        
    def binary(self, num: int)->str:
        
        res = " "
        
        while (num > 0):
            
            if num % 2 == 1:
                res += "1"
            else:
                res += "0"
            
            num //= 2
            
        res = res[::-1]
        
        return res


sol = Clearance()

num = 13
print(f"\nBinary form of the {num} : {sol.binary(num)}")

ith_bit = 2

cleared_num = sol.clear_bit(num, ith_bit)

print(f"\nClearing bit {ith_bit} gives : {sol.binary(cleared_num)}\n")
  
            
        