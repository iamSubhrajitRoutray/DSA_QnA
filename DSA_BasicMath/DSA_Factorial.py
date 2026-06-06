'''Q) Factorial of a given number.'''

num = int(input('Enter the number : '))
    
fact = 1

while (num > 0):

    fact *= num

    num -= 1

print(f'Factorial : {fact}')


