'''Print 1 to N using Recursion'''

# Recursive function to print numbers from current to n
def rec_num(i, n):
    
    # Base case: if current exceeds n, stop recursion
    if i > n:
        return
    
    # Print current number
    print(i)
    
    # Recursive call with next number
    rec_num(i + 1, n)
 

# Driver Code ->   
num = int(input('Enter the number: '))

print('The numbers are: ')

rec_num(1, num)
    
    
    