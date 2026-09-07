'''Check if a number is power of 2 or not.
Q)
Given an integer n, return true if it is a power of two. Otherwise, return false.'''

# An integer n is a power of two if there exists an integer x such that n == 2ˣ.


def is_power_2(num):
    
    power2 = (num & (num - 1))
    
    if power2 == 0:
        return True
    else:
        return False
    

# MAIN/DRIVER CODE:
    
number = 16

answer = is_power_2(number)

if answer:

    print(f"\n{number} is power of 2\n")

else:

    print(f"\n{number} is not a power of 2\n")