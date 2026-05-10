'''Find the Missing Number in the given Array.'''

# def missing_number(arr):
    
#     n = len(arr)
    
#     for i in range(1, n + 1):
        
#         if i not in arr:
#             return i



# array = [4, 6, 1, 8, 2, 3, 7]
# print(array)

# num = missing_number(array)

# print(f'The missing number in the given array is {num}.')



'''DIRECT APPROACH ->
def missing_number(arr):
    
    n = len(arr) + 1
    
    num = (n * (n + 1)) // 2 - sum(arr)
    
    return num


array = [1,2,3,6,5,7]
print(array)

result = missing_number(array)

print(f'The missing number in the given array is {result}.')'''
