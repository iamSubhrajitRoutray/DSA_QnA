'''Check if a number is Palindrome or Not'''

def palindrome(n):
    
    # Initialize a variable to store the reverse of the number
    p_num = 0
    
    # Iterate through each digit of the number until it becomes 0
    
    while n > 0:
        
        # Extract the last digit of the number
        rev = n % 10
        
        # Build the reverse number by appending the last digit
        p_num = p_num * 10 + rev
        
        # Remove the last digit from the original number
        n = n // 10
           
    return p_num



# Main function
num = int(input('enter the number: '))

check_num = palindrome(num)

if check_num == num:
    
    print(f'The given number {num} is a Palindrome.')

else:
    print(f'The number {num} is not a Palindrome.')