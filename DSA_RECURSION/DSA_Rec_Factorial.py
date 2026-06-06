'''Factorial of a number by recursion'''

# Recursive function to calculate factorial of a number
def factorial(n):
    
    # Base case: factorial of 0 is 1
    if n == 1:
        return 1
    
    # Recursive case: n * factorial of (n-1)
    return n * factorial(n - 1)


# Driver code/ Main code - >
num = int(input('Enter the number: '))

# Assigning the factorial function to a variable
result = factorial(num)

# Call the factorial function and print the result
print(f'Factorial of {num} : {result}')