'''Q) Check if a number is Armstrong Number or not'''


def check_armstrong(num):
    
    sum = 0
    
    power = len(str(num))
    
    while num > 0:
        
        last_digit = num % 10
        
        sum += last_digit ** power
        
        num = num // 10
    
    return sum


num = int(input("Enter the number : "))

result = check_armstrong(num)

if result == num:
    
    print(f"YES, {num} is an Armstrong Number.")

else:
    print(f"NO, {num} is not an Armstrong Number.")
            
            
        
            
            
'''Implementing OOPs conpects ->'''

class Armstrong:
    
    def __init__(self, num):
        
        self.num = num
        
        
    def check_armstrong(self):
        
        sum = 0
        
        power = len(str(self.num))
        
        temp = self.num
        
        while temp > 0:
            
            last_digit = temp % 10
            
            sum += last_digit ** power
            
            temp = temp // 10
            
        return sum
    
   
    def display(self):
        
        answer = self.check_armstrong()
        
        if answer == self.num:
            
            print(f"YES, {self.num} is an Armstrong Number.")

        else:
            print(f"NO, {self.num} is not an Armstrong Number.")
            


# Main/Driver code :

number = int(input("Enter the number : "))

result = Armstrong(number)

result.check_armstrong()

result.display()    