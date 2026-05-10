'''Find GCD of two numbers'''

# METHOD 01 -> Brute Force Approach
'''def find_GCD(a, b):

    # Initialize gcd to 1
    gcd = 1
    
    #Iterate from 1 up to the minimum of a and b
    for i in range(1, min(a, b) + 1):
        
        #Check if i is a common factor of both a and b
        if a % i == 0 and b % i == 0:
            
            # Update the gcd to the current common factor i
            gcd = i
            
    # Return the greatest common divisor       
    return gcd


# Main function

num1 = int(input('Enter your first number: '))

num2 = int(input('Enter your second number: '))

result = find_GCD(num1, num2)

print(f'The GCD of {num1} and {num2} numbers is: {result}')'''
    
    
# METHOD 02 -> Built-In 
'''import math

a = int(input('enter the first number: '))

b = int(input('enter the second number: '))

result = math.gcd(a, b)

print(f'The GCD of {a} and {b} numbers is: {result}')'''

# METHOD 03 -> Euclidean Method
def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input('enter the first number: '))

num2 = int(input('enter the second number: '))

result = GCD(num1, num2)

print(f'The GCD of {num1} and {num2} numbers is: {result}')
        
    
        