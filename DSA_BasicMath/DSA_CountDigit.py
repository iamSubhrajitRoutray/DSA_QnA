'''Q) Count digits in a number'''


''' BRUTE FORCE APPRAOCH -> '''

# Function to count the number of digits in an integer.
def count_digit(num):
    
    # Initialize a counter variable
    # 'count' to store the count of digits.
    count = 0

    # If num equals to 0 then return 1; (False)
    if num == 0:
        return 1
        
    # Loop iterates until becomes 0 (no more digits left).  
    while num > 0:
    
        # Increment the counter.
        count += 1
        
        # Divide num by 10 to remove the last digit.
        num = num // 10
    
    return count
        
        
# Main/Driver code : 
if __name__ == "__main__": 
           
    n = int(input('Enter the number: '))
    
    print(f'Your given number is: {n}')
    
    digit = count_digit(n)
    
    print(f'Count of your number : {digit}')
    



''' BETTER APPROACH -> '''

num = int(input('Enter the number: '))

count= 0

while num > 0:
    
    num = num // 10
    
    count = count + 1

print(f'count of your number : {count}')



''' OPTIMAL METHOD -> '''

import math

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

# Main/Driver code : 
if __name__ == '__main__':
    
    num = 12345
    
    print(f' Your number is: {num}')
    
    digit = count_digit(num)
    
    print(f'Count of the digits of given number : {digit}')



        