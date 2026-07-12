'''Minimum days to make M bouquets
Q)
You are given (N) roses and you are also given an array (arr);
where (arr[i]) denotes that the (ith) rose will bloom on the (arr[i]th) day.

You can only pick already bloomed roses that are adjacent to make a bouquet.

You are also told that you require exactly (k) adjacent bloomed roses to make a single bouquet.

Find the minimum number of days required to make at least (m) bouquets each containing (k) roses.
Return -1 if it is not possible.'''


'''BRUTE-FORCE APPROACH'''


def possible_to_make(bloom_days, day, m, k):
    
    count = 0
    
    bouquets = 0
    
    for bloom in bloom_days:
        
        if bloom <= day:
            
            count += 1
            
            if count == k:
                
                bouquets += 1
                count = 0
        else:
            count = 0
    
    return bouquets >= m




def min_days_required(bloom_days, m, k):
    
    min_day = min(bloom_days)
    max_day = max(bloom_days)
    
    total_flowers = m * k
    
    if total_flowers > len(bloom_days):
        return -1
    
    
    for day in range(min_day, max_day + 1):
        
        if possible_to_make(bloom_days, day, m, k):
            return day

    return -1



# Main/Driver code :

bloom_days = [7, 7, 7, 7, 13, 11, 12, 7]

k = 3
m = 2

result = min_days_required(bloom_days, m, k)

if result == -1:
    print(f"Sorry, we cannot make {m} bouquets")
else:
    print(f"We can make {m} bouquets in {result} days.")
    
    
    
    

'''OPTIMAL APPROACH'''


def possible_to_make(bloom_days, day, m, k):
    
    count = 0
    
    bouquets = 0
    
    for bloom in bloom_days:
        
        if bloom <= day:
            
            count += 1
            
            if count == k:
                
                bouquets += 1
                count = 0
        else:
            
            count = 0
    
    return bouquets >= m


def min_days_required(bloom_days, m, k):
    
    low, high = min(bloom_days), max(bloom_days)
    
    answer = 1
    
    total_flowers = m * k
    
    if total_flowers > len(bloom_days):
        return -1
    
    while low <= high:
        
        mid = (low + high) // 2
        
        if possible_to_make(bloom_days, mid, m, k):
            
            answer = mid
            
            high = mid - 1
            
        else:
            low = mid + 1
            
    return answer


                        

# Main/Driver code :

bloom_days = [7, 7, 7, 7, 13, 11, 12, 7]

k = 3
m = 2

result = min_days_required(bloom_days, m, k)

if result == -1:
    print(f"Sorry, we cannot make {m} bouquets")
else:
    print(f"We can make {m} bouquets in {result} days.")
    
            