'''Q) Print all divisors of a given number'''

def divisors(n):
    
    # Create list to store divisors
    div = []
    
    for i in range(1, n + 1):
        
        # Check if i is a divisor of N
        
        if n % i == 0:
            # Add i to result
            
            div.append(i)
    
    # Return the list of divisors
    return div


# Main/Driver code : 
num = int(input('enter the number: '))

result = divisors(num)

print(f'Divisors are : {result}.')

    