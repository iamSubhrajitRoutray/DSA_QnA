'''Count number of bits to be flipped to convert A to B
Q)
Given two integers start and goal. Flip the minimum number of bits of start integer to convert it into goal integer.
A bits flip in the number val is to choose any bit in binary representation of val and flipping it from either 0 to 1 or 1 to 0.'''



def flip_count(start, goal):
    
    temp_num = start ^ goal
    
    count = 0
    
    while temp_num > 0:
        
        if temp_num % 2 == 1:
            
            count += 1
        
        temp_num //= 2
    
    return count


# MAIN/DRIVER CODE:

start = 3
goal = 4

answer = flip_count(start, goal)
print(f"\nNumber of bits flipped : {answer}\n")