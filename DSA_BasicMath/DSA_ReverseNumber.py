'''Reverse Digits of A Number'''

# Function to reverse digits of a number
def reverse_number(n):
    # Variable to store the reversed number
    rev = 0
    
    # Loop until all digits are processed
    while n > 0:
        # Get the last digit
        last_digit = n % 10
        
        # Append it to the reverse number
        rev = rev * 10 + last_digit
        
        # Remove the last number from n
        n = n // 10
    
    # Return the reversed number   
    return rev


# Main function; driver code

num = int(input('Enter the number: '))

print(f'Your number : {num}')

rev_num = reverse_number(num)
    
print(f'Reverse of the number : {rev_num}')