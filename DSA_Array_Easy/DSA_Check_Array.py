'''Given an array of size n, write a program to check if the given array is sorted in (ascending) order or not.
If the array is sorted then return True, Else return False.'''

# def is_sorted(arr):
#     n = len(arr)
    
#     for i in range(n):
        
#         for j in range(i + 1, n):
            
#             if arr[j] < arr[i]:
#                 return False
#     return True


# array = [1,2,3,4,5,6]
# print('The given array is : ',array)
# # Function call ->
# is_sorted(array)

# print('True' if is_sorted(array) else 'False')


'''OPTIMAL METHOD'''

def is_sorted(arr):
    
    n = len(arr)
    
    for i in range(1,n):
        if arr[i] < arr[i - 1]:
            return False
    return True

array = [1,2,3,4,5,6,7,8,9,10]

print(array)

is_sorted(array)

print('True' if is_sorted(array) else 'False')