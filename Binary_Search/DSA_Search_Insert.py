'''Search Insert Position
Q)
You are given a sorted array arr of distinct values and a target value x.
You need to search for the index of the target value in the array.'''


def search(arr,target):
    
    low = 0
    
    high = len(arr) - 1
    
    ans = len(arr)
    
    while low <= high:
        
        mid = (low + high) // 2
        
        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        
        else:
            low = mid + 1
                    
    return ans


# Main/Driver code:
array = [1, 2, 4, 7]

x = 6

index = search(array, x)

print(f"Element {x} inserted at index {index}")