'''Q) Longest SubArray with given Sum K(Positives)'''

def sub_array(arr, k):
    
    n = len(arr)
    
    max_len = 0
    
    for i in range(0, n):
        
        total = 0
        
        for j in range(i, n):
            
            total = total + arr[j]
            
            if total == k:
                max_len = max(max_len, j - i + 1)
                
    return max_len
    

# Main/Driver code : 
array = [10, 5, 2, 7, 1, 9]

k = 15

ans = sub_array(array, k)
 
print(f"Longest subaaray : {ans}")



'''IMPLEMENTING OOPs CONCEPTS.'''

class Sub_Array:
    
    def __init__(self,arr,k):
        self.arr = arr
        self.k = k
        
    def longest(self):
        
        num = len(self.arr)
        
        max_len = 0
        
        for i in range(num):
        
            total_sum = 0
        
            for j in range(i, num):
        
                total_sum += self.arr[j]
        
                if total_sum == self.k:
        
                    max_len = max(max_len, j - i + 1)
                    
        return max_len
    
    def display(self):
        
        print(f"Given array : {self.arr}")
        
        answer = self.longest()
        
        print(f"Longest subarray with sum {self.k} : {answer}")
        


array = [10, 5, 2, 7, 1, 9]

k = 15

result = Sub_Array(array,k)
result.display()
        
    