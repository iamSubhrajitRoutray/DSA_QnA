'''Count the number of set bits
Q)
Given an integer n, return the number of set bits (1s) in its binary representation.
Can you solve it in O(log n) time complexity?'''



'''BRUTE FORCE APPROACH'''


def count_set(num):
    
    count = 1
    
    res = " "
    
    while (num > 0):
        
        if (num % 2 == 1):
            
            res += "1"
            
            count += 1
        
        else:
            
            res += "0"
        
        num //= 2
        
    res = res[::-1]
    
    return count


# MAIN/DRIVER CODE:

number = 13

answer = count_set(number)

print(f"\n{number} has {answer} set bits.\n")
    