'''Q) Check if a number is Palindrome or not'''

def palindrome(n):
    
    # Initialize a variable to store the reverse of the number.
    p_num = 0
    
    # Iterate through each digit of the number until it becomes 0.
    while n > 0:
        
        # Extract the last digit of the number
        rev = n % 10
        
        # Build the reverse number by appending the last digit
        p_num = p_num * 10 + rev
        
        # Remove the last digit from the original number
        n = n // 10
           
    return p_num



# Main/Driver code : 

num = int(input('Enter the number : '))

check_num = palindrome(num)

if check_num == num:
    
    print(f'{num} is a Palindrome.')

else:
    print(f'{num} is not a Palindrome.')
    
    
    
    
'''Implementing OOPs concepts ->'''

class Palindrome:
    
    def __init__(self, num):
        
        self.num = num
        
    def check_palindrome(self):
        
        result_num = 0
        
        temp_num = self.num
        
        while temp_num > 0:
            
            rev_num = temp_num % 10
            
            result_num = result_num * 10 + rev_num
            
            temp_num //= 10
            
        return result_num 
    
    def display(self):
        
        check_num = self.check_palindrome()
        
        if check_num == self.num:
            print(f"YES, the number is a palindrome.")
        
        else:
            print(f"NO, the number is not a palindrome.")


# Main/Driver code : 
       
number =int(input("Enter the number : "))

answer = Palindrome(number)

answer.display()



'''OR : we can also implement our OOPs concepts in a more better way ->'''


class Palindrome:
    
    def __init__(self, num):
        
        self.num = num
    
    def check_plaindrome(self):
    
        result_num = 0
        temp_num = self.num
        
        while temp_num > 0:
            
            rev_num = temp_num % 10
            
            result_num = result_num * 10 + rev_num
            
            temp_num //= 10
            
        return result_num == self.num


# Main/Driver code :

number = int(input("Enter the number : "))

answer = Palindrome(number)

if answer.check_plaindrome():
    print(f"YES, the number is palindrome.")

else:
    print(f"NO, the number is not a palindrome.") 