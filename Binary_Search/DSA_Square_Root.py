'''Finding Sqrt of a number using Binary Search
Q)
You are given a positive integer n. Your task is to find and return its square root.
If (n) is not a perfect square, then return the floor value of sqrt(n).'''


'''BRUTE-FORCE APPROACH'''

def square_root(num):
    
    for i in range(1, num + 1):
        
        square = i * i
        
        if square <= num:
            ans = i
        
        else:
            break
        
    return ans



# Main/Driver code:
n = 49
result = square_root(n)
print(f"The square root of {n} is {square_root(n)}")




'''OPTIMAL APPROACH'''


def square_root(num):
    
    low, high = 0, num//2
    
    ans = 1
    
    while low <= high:
        
        mid = (low + high) // 2  
        
        sq_num = mid * mid
        
        if sq_num <= num:
            
            ans = mid
            
            low = mid + 1
            
        else:
            
            high = mid - 1
            
    return ans
        

# Main/Driver code:
n = 25
result = square_root(n)
print(f"The square root of {n} is {square_root(n)}")
