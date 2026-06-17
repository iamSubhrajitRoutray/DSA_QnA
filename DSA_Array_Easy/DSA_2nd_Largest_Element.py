'''Given an array, find the second smallest and second largest element in the array.'''


'''USING BUILT-IN FUNCTION ->'''

array = [3, 1, 6, 4, 9, 5, 10, 7, 2, 8]

array.sort()

print(f'The sorted array is : {array}')

ele = len(array) - 1

print(f'Second largest element : {ele}')




''' BRUTE FORCE APPROACH -> '''

def second_largest(arr):
    
    n = len(arr)
    
    for i in range(1, n):
        
        key = arr[i]
        
        j = i - 1
        
        while j >= 0 and arr[j] > key:
        
            arr[j + 1] = arr[j]
        
            j -= 1
        
        arr[j + 1] = key
    
    print(arr)


# Main/Driver code :

array = [3, 1, 6, 4, 9, 5, 10, 7, 2, 8]

print(f'Given array :')

second_largest(array)

ele = array[len(array) - 2]

print(f'Second largest element : {ele}')




''' OPTIMAL APPROACH -> ''' 

from math import inf


def second_largest(arr):
    
    largest = float(-inf)
    
    second_largest = float(inf)
    
    n = len(arr)
    
    for i in range(n):
       
        if arr[i] > largest:
          
            second_largest = largest
          
            largest = arr[i]
       
        elif arr[i] > second_largest and arr[i] != largest:
       
            second_largest = arr[i]
    
    return second_largest


# Main/Driver code :

array = [3, 1, 6, 4, 9, 5, 10, 7, 2, 8]

print('Given array : ', array)

ele = second_largest(array)

print(f'Second largest element : {ele}')





'''IMPLEMENTING OOPs CONCEPTS.'''


from math import inf


class Second_Largest:
    
    def __init__(self,arr):
        self.arr = arr
    
    def element(self):
        
        num = len(self.arr)
        
        largest = float(-inf)
        second_large = float(-inf)
        
        solve_arr = self.arr
        
        for i in range(num):
            if solve_arr[i] > largest:
                
                second_large = largest
                largest = solve_arr[i]
                
            elif solve_arr[i] > second_large and solve_arr[i] != largest:
                second_large = solve_arr[i]
                
        return second_large
    
    def display(self):
       
        print(f"Given array : {self.arr}")
        
        ele = self.element()
        
        print(f"Second largest element in array : {ele}")
        

# Main/Driver code :

array = [3, 1, 6, 4, 9, 5, 10, 7, 2, 8]

answer = Second_Largest(array)

answer.display()       
