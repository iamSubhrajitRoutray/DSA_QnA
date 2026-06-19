'''Q) Given an array, we have to find the largest element in the array.'''



''' BRUTE FORCE APPROACH -> '''

# Function to find the largest element
def largest_elemnt(arr):
    
    n = len(arr)
    
    for i in range(n):
        # we just assumed i to be the smallest and stored a variable as min_index to be i
        min_index = i       
        
        for j in range(i + 1, n):
        
            # If value of j which is to be found smaller than our min_index then ->
            if arr[j] < arr[min_index]:
            
                # Store min_index as index of j
                min_index = j
                
        # The elements are then swapped.       
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    print(arr)
# In the above function we have used SELECTION SORT
# It sort out the elements in the given array in ascending order.
    
    
# Main Driver code ->
array = [3, 6, 1, 8, 2, 7, 4]

largest_elemnt(array)

# As we now our array is sorted in ascending form so we called the value stored in last index.
ele = array[len(array) - 1]

print(f'Largest element : {ele}')




''' OPTIMAL APPROACH -> '''

def largest_element(arr):
    
    max_ele = arr[0]     # We set a variable named max to be the value at index 0
    
    n = len(arr)
    
    for i in range(1, n):        # This loop runs for i from index 1 to n-1
        
        if arr[i] > max_ele:         # if the value of i at any index other than the max found to be greater then ->
            max_ele = arr[i]         # we set that value to be the max value
            
    return max_ele                   # in the end we return the max value



# Main Driver code ->

array = [3, 6, 2, 5, 1, 8, 4, 9]

print('Given array : ', array)

ele = largest_element(array)

print(f'Largest element : {ele}')







'''IMPLEMENTING OOPs CONCEPTS.'''

# OPTIMAL APPROACH ->

class Element:
    
    def __init__(self,arr):
        self.arr = arr
        
    def largest(self):
        
        max_ele = self.arr[0]
        
        n = len(self.arr)
        
        for i in range(1, n):
            
            if self.arr[i] > max_ele:
            
                max_ele = self.arr[i]
            
        return max_ele
    
    def display(self):
        
        print(f"Given array : {self.arr}")
        
        print(f"Largest element : {self.largest()}")
        
        
# Main/Driver code :

array = [3, 6, 2, 5, 1, 8, 4, 9]

result = Element(array)

result.display()
