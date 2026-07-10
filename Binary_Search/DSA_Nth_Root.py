'''Nth Root of a Number using Binary Search
Q)
Given two numbers N and M, find the Nth root of M.
The nth root of a number M is defined as a number X when raised to the power N equals M.
If the 'nth root is not an integer, return -1.'''



'''BRUTE-FORCE APPROACH'''

def find_root(m, n):
    
    for i in range(1, m+1):
        ans = i ** n
        
        if ans == m:
            return i
        
        if ans > m:
            break
        
    return -1



# Main/Driver code :
n = 3
m = 27

print(find_root(m, n))




'''OPTIMAL APPROACH'''

def find_root(m, n):
    
    low = 0
    high = m
    
    
    while low <= high:
        
        mid = (low + high) // 2
        
        ans = 1
        
        for _ in range(n):
            
            ans = ans * mid

            if ans > m:
                break
        
        if ans == m:
            return mid
     
        if ans < m:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1


# Main/Driver code :
n = 3
m = 27

print(find_root(m, n))
