'''Check if a number is odd or not
Q)
Given a non-negative integer n, determine whether it is odd
Return true if the number is odd, otherwise return false.'''

# A number is odd if it is not divisible by 2 (i.e., n % 2 != 0).

def check_odd_even(num):
    
    if (num % 2 == 1):
       
        return True

    return True


# MAIN/DRIVER CODE:

number = 5
answer = check_odd_even(number)
print(f"\n{answer}\n")
    
    