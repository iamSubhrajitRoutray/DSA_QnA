'''Q) Given an integer array sorted in non-decreasing order,
remove the duplicates in place such that each unique element appears only once.
If there are k elements after removing the duplicates,
then the first k elements of the array should hold the final result.
It does not matter what you leave beyond the first k elements.'''



''' BRUTE FORCE APPROACH -> '''

def remove_duplicate(arr):
    
    n = len(arr)
    
    freq_list = {}
    
    for i in range(n):
    
        freq_list[arr[i]] = 0
        
    j = 0
    
    for key in freq_list:
        
        arr[j] = key
        
        j += 1
    
    return print(f"Total no. of elements : {j}.")

# Main/Driver code :
array = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4]

remove_duplicate(array)





''' OPTIMAL APPROACH -> '''

def duplicate(arr):
    
    n = len(arr)
    
    i = 0
    j = i + 1
    
    if n == 1:
        return 1
    
    while j < n:
        
        if arr[j] != arr[i]:
            
            i += 1
            
            arr[i], arr[j] = arr[j], arr[i]
        
        j += 1
    
    return print(f"Actual no. of elements : {i + 1}")
    
    
# Main/Driver code :
array = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4]

duplicate(array)




'''IMPLEMENTING OOPs CONCEPTS.'''


# OPTIMAL APPROACH -> 

class Element:
    
    def __init__(self,arr):
        self.arr = arr
    
    def duplicate(self):
        
        n = len(self.arr)

        i = 0
        j = i + 1
        
        while j < n:
            
            if self.arr[j] != self.arr[i]:
                
                i += 1
                
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            
            j += 1
            
        return (i + 1)
    
    
    def display(self):
    
        print(f"Given array : {self.arr}")
        
        answer = self.duplicate()
        
        print(f" No. of original elements : {answer}")
        

# Main/Driver code :

array = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4]

result = Element(array)
result.display()



# BRUTE FORCE APPRAOCH ->

class Element:

    def __init__(self, arr):
        self.arr = arr
        
    def duplicate(self):
    
        n = len(self.arr)
    
        freq_list = {}
    
        for i in range(n):
    
            freq_list[self.arr[i]] = 0
        
        j = 0
    
        for key in freq_list:
        
            self.arr[j] = key
        
            j += 1
    
        return j
    
    def display(self):
        
        print(f"Given array : {self.arr}")
        
        answer = self.duplicate()
        
        print(f"No. of original elements : {answer}")


# Main/Driver code :

array = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4]

result = Element(array)
result.display()
