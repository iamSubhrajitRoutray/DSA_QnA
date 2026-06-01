'''HASHING Brute Force Method'''

# Given array
arr = [1, 3, 1, 3, 1, 2, 3]

# Hash array: we gonna use it as for maping the frequency of number/strings appearing in array given to us.
hash_arr = [1, 2, 3, 4, 5]

count = 0   # Initialize count to 0

# for loop used to loop over the hash array
for num in hash_arr:
    
    count = 0
    
    # for index taken as i (variable) to search over the given array
    for i in arr:
        
        #if our number in hash array matches the number in given array...
        if i == num:
            
            #...increase the count by +1
            count += 1
        
    print(count)
    
arr =[]

num = int(input('enter the lenght of your array: '))

print(num)

for i in range(num):

    val = input('Enter the value: ')

    arr.append(val)

print(arr)





'''OPTIMAL APPROACH ->'''

arr = [1, 4, 2, 1, 3, 1, 2, 6, 3, 1, 2]

hash_arr = [1, 3, 4, 6, 2, 8, 11, 10]
   
hash_list = [0] * 11

for num in arr:
    
    hash_list[num] += 1
    
for num in hash_arr:
    
    if num < 1 or num > 10:
        
        print(0)
    
    else:
    
        print(hash_list[num])