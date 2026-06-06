'''Reverse a given Array'''

def reverse_array(arr):
    
    # Get the length of the input array
    l = len(arr)
    
    # Create a new array of same size to store reversed elements
    new_arr = [0] * l
    
    # Start a loop to fill n_arr[] from the back of arr[]
    for i in range(l):
        
        # Place elements from the end of arr into the start of n_arr
        new_arr[i] = arr[l - i - 1]
        
     # Return the reversed array    
    return new_arr


# To reverse an array/list.

num = int(input('Enter array lenght : '))

new_arr = []

for i in range(num):
    
    val = input(f'Enter the value {i+1}: ')

    new_arr.append(val)


print(f'Given list : ', new_arr)

rev_arr = reverse_array(new_arr)

print(f'Reverse of list : ',rev_arr)
    

# Main/Driver code :
new = [10, 20 ,30, 40, 50, 60, 70, 80, 90, 100]

rev = reverse_array(new)

print(rev)


'''In-Build Function Module'''

# Function to reverse the array using slicing
def reverse_array(arr):
    
    # Reassign the array with reversed version using slicing
    arr[:] = arr[::-1]
    
    
# Main/Driver code :
new_arr = [1, 2, 3, 4, 5, 6]

rev = reverse_array(new_arr)

print(rev)






# HOW SLICING WORKS..!?

'''Python Slicing — How It Actually Works

Slicing returns a new sequence (it does NOT modify the original—unless you assign back).

Example Setup

arr = [10, 20, 30, 40, 50]

Indexes:

Index:   0   1   2   3   4
Value:  10  20  30  40  50

1) Basic Slicing

arr[1:4]

Start at index 1
Stop before index 4

Result:

[20, 30, 40]

2) Default Values

arr[:3] → [10, 20, 30]
arr[2:] → [30, 40, 50]
arr[:] → [10, 20, 30, 40, 50]

Expression -> Meaning
[:end] -> from start
[start:] -> till end
[:] -> full copy

3) Step (Skipping Elements)

arr[::2]

Take every 2nd element

Result:

[10, 30, 50]


4) Reverse Using Slicing

arr[::-1]

Step = -1 → move backward

Result:

[50, 40, 30, 20, 10]


Important Concept: New List vs Same List

This creates a new list -->

new_arr = arr[::-1]

This modifies original list -->

arr[:] = arr[::-1]


Negative indexing:

arr[-1] → last element (50)
arr[-3:] → [30, 40, 50]'''
