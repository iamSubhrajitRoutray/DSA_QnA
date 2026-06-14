'''3 Sum : Find triplets that add up to a zero
Q)
Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero.
In short, you need to return an array of all the unique triplets;
[arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i, and their sum is equal to zero.'''


'''BRUTE FORCE APPROACH ->'''

def threesum(arr):
    
    n = len(arr)
   
    myset = set()
    
    for i in range(n):
        
        for j in range(i + 1, n):
        
            for k in range(j + 1, n):
        
                if arr[i] + arr[j] + arr[k] == 0:
        
                    temp = [arr[i], arr[j], arr[k]]
        
                    temp.sort()
        
                    myset.add(tuple(temp))
                    
    
    return [list(ans) for ans in myset]


# Main/Driver code :
array = [-1, 0, 1, 2, -1, -4]

result = threesum(array)
print(result)
    
    
    
    
    
'''OPTIMAL APPROACH ->'''

def three_sum(arr):
    
    n = len(arr)
    
    ans = []
    
    arr.sort()
    
    for i in range(n):
    
        if arr[i] != 0 and arr[i] == arr[i-1]:
            continue
    
        j = i + 1
        k = n - 1
    
        while j < k:
          
            total_sum = arr[i] + arr[j] + arr[k]
          
            if total_sum < 0:
                j += 1
          
            elif total_sum > 0:
                k -= 1
          
            else:
                temp = [arr[i],arr[j],arr[k]]
                ans.append(temp)
          
                j += 1
                k -= 1
        
        while j < k and arr[j] == arr[j - 1]:
            j += 1
        
        while j < k and arr[k] == arr[k + 1]:
            k -= 1
    
    return ans


# Main/Driver code :
array = [-1, 0, 1, 2, -1, -4]

result = three_sum(array)
print(result)

    
    

                
