'''4 Sum | Find Quads that add up to a target value
Q)
Given an array of N integers,
your task is to find unique quads that add up to give a target value.
In short, you need to return an array of all the unique quadruplets [arr[a], arr[b], arr[c], arr[d]]
such that their sum is equal to a given target.'''



'''BRUTE-FORCE APPROACH ->'''


def four_sum(arr,target):
    
    n=len(arr)
    
    myset = set()
    
    for i in range(0, n):
    
        for j in range(i + 1, n):
    
            for k in range(j + 1, n):
    
                for l in range(k + 1, n):
    
                    total = arr[i] + arr[j] + arr[k] + arr[l]
    
                    if total == target:
    
                        temp = [arr[i], arr[j], arr[k], arr[l]]
                        temp.sort()
    
                        myset.add(tuple(temp))
    
    return [list(ans) for ans in myset]


# Main/Driver code:

array = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]

target = 9

result = four_sum(array, target)

print(result)




'''BETTER APPROACH ->'''


def four_sum(arr,target):
    
    n = len(arr)
    
    myset = set()
    
    for i in range(0, n):
        
        for j in range(i + 1, n):
        
            seen_num = set()
        
            for k in range(j + 1, n):
        
                forth_num = target - (arr[i] + arr[j] + arr[k])
        
                if forth_num in seen_num:
        
                    temp = [arr[i], arr[j], arr[k], forth_num]
                    temp.sort()
        
                    myset.add(tuple(temp))
        
                seen_num.add(arr[k])
    
    return [list(ans) for ans in myset]


# Main/Driver code:

array = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]

target = 9

result = four_sum(array, target)

print(result)     




'''OPTIMAL APPROACH ->'''          
            
            
def four_sum(arr, target):
    
    n = len(arr)
    
    result = []
    
    arr.sort()
    
    for i in range(n):

        if i > 0 and arr[i] == arr[i - 1]:
            continue

        for j in range(i + 1, n):

            if j > (i + 1) and arr[j] == arr[j - 1]:
                continue

            k = j + 1
            l = n - 1

            while k < l:

                total = arr[i] + arr[j] + arr[k] + arr[l]
                
                if total == target:
                
                    result.append([arr[i], arr[j], arr[k], arr[l]])
                
                    k += 1
                    l -= 1

                    while k < l and arr[k] == arr[k - 1]:
                        k += 1

                    while l > k and arr[l] == arr[l + 1]:
                        l -= 1

                elif total < target:
                    k += 1

                else:
                    l -= 1

    return result


# Main/Driver code:

array = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]

target = 9

result = four_sum(array, target)

print(result)     
    
    