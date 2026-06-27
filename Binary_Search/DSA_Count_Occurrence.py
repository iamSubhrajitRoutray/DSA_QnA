'''Count Occurrences in Sorted Array
Q)
You are given a sorted array containing N integers and a number X,
you have to find the occurrences of X in the given array'''


'''BRUTE-FORCE APPROACH'''

def count(arr, x):

    count = 0

    for i in range(len(arr)):

        if arr[i] == x:

            count += 1

    return count


# Main/Driver code :

array = [2, 2 , 3 , 3 , 3 , 3 , 4]

print(f"Given array : {array}")

x = 3 

answer = count(array, x)

print(f"Number {x} appeared {answer} times in the array.")




'''OPTIMAL APPROACH'''


class Occurrence:
    
    def __init__(self, arr, x):
        self.arr = arr
        self.x = x
    
    
    def lower_bound(self):
        
        n = len(self.arr)
        
        low, high = 0, n-1
        
        lb = -1
        
        while low <= high:
            
            mid = (low + high) // 2
            
            if self.arr[mid] >= self.x:
        
                lb = mid
        
                high = mid - 1
            
            else:
        
                low = mid + 1
        
        return lb
    
    
    def upper_bound(self):
        
        n = len(self.arr)
        
        low, high = 0, n-1
        
        ub = n
        
        while low <= high:
        
            mid = (low + high) // 2
             
            if self.arr[mid] > self.x:
        
                ub = mid
        
                high = mid - 1
        
            else:
        
                low = mid + 1
        
        return ub
    
    
    def count(self):
        
        lower = self.lower_bound()
        
        if lower == -1:
            return 0
        
        upper = self.upper_bound()
        
        count = upper - lower
        
        return count
    
        
# Main/Driver code :

array = [2, 2 , 3 , 3 , 3 , 3 , 4]
print(f'Given array : {array}')

x = 3

answer = Occurrence(array, x)

print(f"Number {x} appeared {answer.count()} times in the array.")