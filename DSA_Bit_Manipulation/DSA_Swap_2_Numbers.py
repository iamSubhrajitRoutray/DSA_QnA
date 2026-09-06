'''Swap two numbers
Q)
Given two integers a and b, swap them in-place using only 2 variables (without using a temporary variable).'''


def swap_num(a, b):
    
    a = a ^ b      # Equation 1
    
    b = a ^ b      # Equation 2
    
    a = a ^ b      # Equation 3
    
    return a, b


x = 12

y = 15

res = swap_num(x, y)

print(f"\nSwapping value of (x, y) : {x, y} = {res}\n")




'''Here's the intuition :'''
    
# As we know ^ = XOR Operator, now when we get

# (a = a ^ b)

# (b = a ^ b).

# Here we can write (b = (a ^ b) ^ b )

# It is so because we put the value of a in place of a in the equation 2.
# Thus b and b cancels out; remains:-
 
# (b = a)      # Equation 4

# Now again we are bring (a = a ^ b).

# We can also write this as (a = (a ^ b) ^ b ); as per the equation 1.

# But we know from equation 4 that (b = a). So putting the value,

# (a = (a ^ b) ^ a)

# Here a and a get cancels out; remains 

# a = b       # Equation 5

# Thus from equation 4 and equation 5 we can see the initial values are been swapped.


# Point to remember: anything XOR 0 is 1.
