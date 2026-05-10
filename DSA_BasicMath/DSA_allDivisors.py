'''Print all Divisors of a given Number'''

def divisors(n):
    # Create list to store divisors
    div = []
    
    for i in range(1,n+1):
        # Check if i is a divisor of N
        
        if n % i ==0:
            # Add i to result
            
            div.append(i)
    # Return the list of divisors
    
    return div

# Driver code ->
num = int(input('enter the number: '))

result = divisors(num)

print(f'The divisors of {num} are {result}.')

    