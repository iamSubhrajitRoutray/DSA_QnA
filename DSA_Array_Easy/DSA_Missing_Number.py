'''Q) Find the Missing Number in the given Array.'''



''' BRUTE FORCE APPROACH -> '''

def missing_number(arr):
    
    n = len(arr)
    
    for i in range(1, n + 1):
        
        if i not in arr:
            return i


# Main/Driver code : 
array = [4, 6, 1, 8, 2, 3, 7]

print(array)

num = missing_number(array)

print(f' Missing number : {num}.')




''' DIRECT APPROACH -> '''

def missing_number(arr):
    
    n = len(arr) + 1
    
    num = (n * (n + 1)) // 2 - sum(arr)
    
    return num


# Main/Driver code : 
array = [1, 2, 3, 6, 5, 7]

print(array)

result = missing_number(array)

print(f'Missing number : {result}.')





'''IMPLEMENTING OOPs CONCEPTS.'''


# BRUTE FORCE APPROACH -> 

class solution:
    
    def __init__(self,arr):
        self.arr = arr
        
    def missing(self):
        
        n = len(self.arr)
        
        for i in range(1, n + 1):
        
            if i not in self.arr:
                return i
    

    def display(self):
        
        print(f"Given array : {self.arr}")
        
        ans = self.missing()
        
        print(f"The missing number : {ans}")
        
# Main/Driver code :
array = [4, 6, 1, 8, 2, 3, 7]

res = solution(array)
res.display()



# DIRECT APPROACH -> 

class missing:

    def __init__(self,arr):
        self.arr = arr

    def number(self):

        n = len(self.arr) + 1

        res = (n * (n + 1)) // 2 - sum(self.arr)
 
        return res

    def display(self):

        print(f"Given array : {self.arr}")

        print(f"Missing number : {self.number()}")
        
# Main/Driver code :

array = [4, 6, 1, 8, 2, 3, 7]

res = missing(array)
res.display()