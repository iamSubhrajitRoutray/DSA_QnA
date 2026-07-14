'''Find the Smallest Divisor Given a Threshold
Q)
You are given an array of integers 'arr' and an integer i.e. a threshold value 'limit'.
Your task is to find the smallest positive integer divisor, such that upon dividing all the elements of the given array by it,
the sum of the division's result is less than or equal to the given threshold value.'''



'''BRUTE_FORCE APPROACH'''


from math import ceil

def find_smallest_divisor(arr, limit):

    max_val = max(arr)
    
    for div in range(1, max_val + 1):
        
        total_sum = 0
        
        for num in arr:
            
            total_sum += ceil(num/div)
            
        if total_sum <= limit:
            return div
    return -1



# Main/Driver code:

array = [1, 2, 3, 4, 5]

target = 8

answer = find_smallest_divisor(array, target)

print(answer)






'''OPTIMAL APPROACH'''


def find_total_sum(arr, mid):
    
    total = 0
    
    for num in arr:
        
        total += ceil(num/mid)
    return total
    


def find_smallest_divisor(arr, limit):
    
    low = 1
    high = max(arr)
    
    while low <= high:
        
        mid = (low + high) // 2
        
        res = find_total_sum(arr, mid)
        
        if res <= limit:
            res = mid
    
        return res
    
    return -1



# Main/Driver code:

array = [1, 2, 3, 4, 5]

target = 8

answer = find_smallest_divisor(array, target)

print(answer)
