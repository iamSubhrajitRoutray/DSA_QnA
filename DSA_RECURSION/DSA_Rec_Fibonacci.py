'''Print Fibonacci Series up to Nth term'''

'''RECURSIVE METHOD : '''

def fibonacci(n):
    # Base case: if N is 0 or 1, return N
    if n <= 1:
        return n
    
    # Recursive calls: calculate previous two terms
    last = fibonacci(n - 1)      # (n-1)th term; the previous term of the current term
    s_last = fibonacci(n - 2)    # (n-2)th term; the previous than the previous term of the current term
    
    return last + s_last

# # Main/Driver code :
num = int(input('Enter the number: '))

print(f'Fibonacci series till {num} is: ')


# Since this function will only print the last term of the series if being called direcly;

# To show all the numbers to the nth term, we have to loop it to the (n+1)th term (as index starts from 0)
for i in range(num + 1):
    
    print(fibonacci(i), end=' ')
    
# Use for removing the balnk space
print()




''' METHOD 02 '''

def fibonacci(n):
    
    if n == 0:
        
        print(0)
   
    elif n == 1:
        
        print('0 1')
   
    else:
        
        fib = [0] * (n + 1)
      
        fib[0] = 0
      
        fib[1]= 1
        
        for i in range(2, n + 1):
      
            fib[i] = fib[i - 1] + fib[i - 2]
        
    
    print(' '.join(str(val) for val in fib))
    

num = int(input('Enter the number: '))

print(f'Fibonacci series till {num}th term : ', fibonacci(num))