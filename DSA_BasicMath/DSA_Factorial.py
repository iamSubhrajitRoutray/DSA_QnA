'''Q) Factorial of a given number.'''

# num = int(input('Enter the number : '))
    
# fact = 1

# while (num > 0):

#     fact *= num

#     num -= 1

# print(f"Factorial : {fact}")





'''Implementing OOPs concepts ->'''

class Factorial:
        
    def __init__(self, num):
        
        self.num = num
        
    def find_factorial(self):
        
        fact = 1
        
        while self.num > 0:
        
            fact *= self.num
        
            self.num -= 1
        
        return fact
            
    def display(self):
        
        answer = self.find_factorial()
        
        print(f"Factorial : {answer}")
        
        
# Main/Driver code :

number = int(input("Enter the number : "))

result = Factorial(number)

result.display()
        