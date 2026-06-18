'''Q) Print all divisors of a given number.'''

class Divisors:
    def find_divisors(self, n):
        
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
num = int(input("Enter the number: "))

obj = Divisors()

result = obj.find_divisors(num)

print(f"Divisors are : {result}.")




''' IMPLEMENTING OOPs CONCEPTS : '''


class Find_Divisors:
    
    def __init__(self, num):
         self.num = num
         self.div = []
    
    def divisors(self):
        
        for i in range(1, self.num + 1):
            
            if self.num % i == 0:
                self.div.append(i)
                
    def display(self):
        print(f"Divisors of {self.num} are {self.div}.")
        

# Main/Driver code :

number = int(input("Enter the number : "))

finder = Find_Divisors(number)

finder.divisors()
finder.display()
    