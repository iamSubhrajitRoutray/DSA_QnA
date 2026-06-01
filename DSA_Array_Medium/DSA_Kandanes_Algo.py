'''Kadane's Algorithm : Maximum Subarray Sum in an Array'''



''' BRUTE FORCE APPROACH '''

def max_sum(arr):
    
    l = len(arr)
    
    max_sum = float('-inf')
    
    for i in range(0, l):
        
        total = 0
        
        for j in range(i, l):
            
            total = total + arr[j]
            
            max_sum = max(total, max_sum)
            
    print(max_sum)
    
array = [2, 3, 5, -2, 7, -4]

max_sum(array)
            
            


'''OPTIMAL APPROACH'''

def max_sum(arr):
    
    l = len(arr)
    
    total_sum = 0
    
    max_sum = float('-inf')
    
    for i in range(0, l):
        
        total_sum = total_sum + arr[i]
        
        max_sum = max(max_sum, total_sum)
        
        if total_sum < 0:
            total_sum = 0
    
    print(max_sum)
    

array = [2, 3, 5, -2, 7, -4]

max_sum(array)


    