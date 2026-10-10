'''Print Name N times using Recursion'''

# Recursive function to print name n times
def name_print(name, n):
    
    # Stops recursion when n becomes 0; Prevents infinite recursion
    if n == 0:
        
        return
    
    # Prints the name once per function call
    print(name)
    
    # Calls the function again; Reduces n by 1
    return name_print(name, n - 1)


# Main/Driver code :
user_name = input('Enter your name: ')

num = int(input('Enter the number of times you want to print your name: '))

name_print(user_name, num)
    
    