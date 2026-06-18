'''Q) Given an array of size n,
write a program to check if the given array is sorted in (ascending) order or not.
If the array is sorted then return True, Else return False.'''



''' BRUTE FORCE -> '''

def is_sorted(arr):
    
    n = len(arr)
    
    for i in range(n):
        
        for j in range(i + 1, n):
            
            if arr[j] < arr[i]:
                return False
    return True


array = [1, 2, 3, 4, 5, 6]
print('Given array is : ', array)

# Function call ->
is_sorted(array)

print('True' if is_sorted(array) else 'False')




'''OPTIMAL METHOD'''

def is_sorted(arr):
    
    n = len(arr)
    
    for i in range(1, n):
        
        if arr[i] < arr[i - 1]:
            return False
    
    return True

# Main/Driver code :
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(array)

is_sorted(array)

print('True' if is_sorted(array) else 'False')




'''IMPLEMENTING OOPs CONCEPTS.'''


# BRUTE FORCE APPROACH ->

class Check_Array:
    
    def __init__(self, arr):
        self.arr = arr

    def is_sorted(self):
        
        num = len(self.arr)
        
        for i in range(0, num):
            
            for j in range(i + 1, num):
            
                if self.arr[j] < self.arr[i]:
            
                    return False
            
            return True
    
    def display(self):
        
        check = is_sorted(self.arr)
        
        print(f"Given array : {self.arr}")
        
        print("True" if check else "False")


# Main/Driver code :

array_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a1 = Check_Array(array_1)
a1.display()

array_2 = [1, 2, 3, 5, 7, 4, 6, 8, 9, 10]

a2 = Check_Array(array_2)
a2.display()




# OPTIMAL APPROACH

class Check_Array:
    
    def __init__(self, arr):
        self.arr = arr
        
    def is_sorted(self):
        
        num = len(self.arr)
        
        for i in range(1, num):
            
            if self.arr[i] < self.arr[i-1]:
                
                return False
        return True
    
    def display(self):
        
        check = self.is_sorted()
        
        print(f"Given array is : {self.arr}")
        
        print("True" if check else "False")
        

# Main/Driver code :

array_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a1 = Check_Array(array_1)
a1.display()

array_2 = [1, 2, 3, 5, 7, 4, 6, 8, 9, 10]

a2 = Check_Array(array_2)
a2.display()

