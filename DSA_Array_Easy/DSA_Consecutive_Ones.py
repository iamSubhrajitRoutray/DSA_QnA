'''Q) Given an array that contains only 1 and 0;
return the count of maximum consecutive ones in the array.'''


''' OPTIMAL APPRAOCH -> '''

def maximum_consecutive(arr):
    
    n = len(arr)
    
    count = 0
    
    max_one = 0
    
    for i in range(n):
    
        if arr[i] == 1:
            count += 1
    
        else:
            count = 0
        
        max_one = max(max_one, count)
    
    return max_one

array = [1, 2, 1, 1, 1, 3, 1, 1, 4]

res = maximum_consecutive(array)

print(f"Maximum consecutive 1's in array : {res}.")



'''IMPLEMENTING OOPs CONCEPTS.'''

class Consecutive:
    
    def __init__(self, arr):
        self.arr = arr
    
    def max_consecutive(self):
        
        num = len(self.arr)
        count = 0
        max_count = 0

        for i in range(num):
            
            if self.arr[i] == 1:
                count += 1
                
            else:
                count = 0
                
            max_count = max(max_count, count)

        return max_count
    
    def display(self):
        result = self.max_consecutive()
    
        print(f"Given array : {self.arr}")
        
        print(f"Maximum consecutive 1's : {result}")
        

# Main/Driver code :

array = [1, 2, 1, 1, 1, 3, 1, 1, 4]

answer = Consecutive(array)
answer.display()