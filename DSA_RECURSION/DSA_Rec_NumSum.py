'''Sum of first N Natural Numbers'''


''' BRUTE FORCE APPROACH -> '''

# Function to find sum of first N natural numbers using loop
def num_sum(n):

    # Initialize sum to 0
    total = 0
    # Loop from 1 to N
    for i in range(1, n + 1):
    
         # Add current number to sum
        total += i
        
    # Return the calculated sum
    return total

# Driver/Main code ->
num = int(input('enter the number: '))

# Assigning a variable to the sum_num() function
sum = num_sum(num)

# Print the result i.e the (sum)
print(f'The sum total of all natural numbers from 1 to {num} is {sum}')






'''RECURSIVE METHOD''' 

# Recursive function to find sum of first N natural numbers
def num_sum(n):
    
    # Base case: if N is 1, return 1
    if n == 1:
        return 1
    
     # Recursive case: current number + sum of previous numbers adn loop until it return -1 or False.
    return n + num_sum(n-1)


# Driver/Main code ->
num = int(input('Enter the number: '))

sum = num_sum(num)

print(f'Sum of natural numbers {num} : {sum}')
    
    
    
    

'''USING FORMULA ->''' 

# Function to find sum of first N natural numbers using formula  
def num_sum(n):
    if n == 1:
        return 1
        
    # Apply the based formula directly
    return (n * (n + 1)) // 2
    
# Driver/Main code ->
num = int(input('Ennter Number: '))

sum = num_sum(num)

print(f'Sum of natural numbers {num} : {sum}')
    