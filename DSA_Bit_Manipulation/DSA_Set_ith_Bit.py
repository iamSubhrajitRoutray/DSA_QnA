'''Set the i-th bit'''

# This question says that for a given bit we have to set it i.e. toggle it to '1'.


class SET:

    def set_the_bit(self, num, i):
        
        set_bit = (num | (1 << i))
        
        return set_bit


    # TO CHECK:

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

sol = SET()

num = 13

print(f"\nBinary form of {num} : {sol.binary(num)}")

i = 1

num_set = sol.set_the_bit(num, i)

print(f"\nAfter bit Set: {sol.binary(num_set)}: {num_set}\n")