'''Count digits in a number'''

#METHOD 01-->
# Function to count the number
# of digits in an integer 'n'.
def count_digit(num):
    # Initialize a counter variable
    # 'count' to store the count of digits.
    
    count = 0

    #if num equals to 0 then return 1; (False)
    
    if num == 0:
        return 1
        
    # While loop iterates until 'n'
    # becomes 0 (no more digits left).  
    
    while num > 0:
    
        # Increment the counter
        # for each digit encountered.
        
        count += 1
        
        # Divide 'n' by 10 to
        # remove the last digit.
        
        num = num // 10
        
    # Return the
    # count of digits.
    
    return count
        
# Main function
if __name__ == "__main__":        
    n = int(input('Enter the number: '))
    print(f'Your given number is: {n}')
    digit = count_digit(n)
    print(f'The digit count of your number is: {digit}')
    

#METHOD 02-->

'''num = int(input('enter the number: '))
count= 0
while num>0:
    num = num//10
    count=count+1

print(f'the digit count of your number is {count}')'''

#METHOD 03-->

'''import math

# Calculate the count of digits in 'n'
# using logarithmic operation log10(n) + 1.

def count_digit(n):
    # Initialize a variable 'count' to
    # store the count of digits.
    
    count = int(math.log10(n) + 1)
    
    # The expression int(math.log10(n) + 1)
    # calculates the number of digits in 'n'
    # and casts it to an integer.
    
    # Adding 1 to the result accounts
    # for the case when 'n' is a power of 10,
    # ensuring that the count is correct.
   
    # Finally, the result is cast
    # to an integer to ensure it is rounded
    # down to the nearest whole number.
    
    # Return the count of digits in 'n'.
    
    return count

# Main function
if __name__ == '__main__':
    
    num = 12345
    
    print(f'Your given number is: {num}')
    
    digit = count_digit(num)
    
    print(f'The count of the digit of given number is: {digit}')'''



        