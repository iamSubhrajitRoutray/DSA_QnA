'''Factorial of a given number.'''

num = int(input(''))
    
fact = 1

while (num > 0):

    fact *= num

    num -= 1

print(f'Factorial : {fact}')


