'''Koko Eating Bananas
Q)
Each hour, the monkey chooses a non-empty pile of bananas and eats (k) bananas.
If the pile contains less than (k) bananas, then the monkey consumes all the bananas and would not eat any more bananas in that hour.

Find the minimum number of bananas (k) to eat per hour so that the monkey can eat all the bananas within (h) hours.'''



'''BRUTE-FORCE APPROACH'''

from math import ceil



def count_hours(Piles, hourly):
    
    total_hours = 0
    
    for pile in Piles:
        
        total_hours = total_hours + ceil(pile / hourly)
        
    return total_hours



def min_no_of_bananas(Piles, hr):
    
    max_banana = max(Piles)
    
    for i in range(1, max_banana):
        
        hours = count_hours(Piles, i)
        
        if hours <= hr:
            return i
        
    return -1



# Main/Driver code:

piles = [7, 15, 6, 3]

hour = 8

answer = min_no_of_bananas(piles, hour)


if answer == -1:

    print(f"Koko cannot be able to eat in {hour} hours !")

else:
    
    print(f" Koko can eat in {answer} bananas in {hour} hours.")
    
    
    
    
    
    
'''OPTIMAL APPROACH'''


def count_hours(Piles, hourly):
    
    total_hours = 0
    
    for pile in Piles:
        
        total_hours += ceil(pile / hourly)
        
    return total_hours



def no_of_bananas(Piles, hr):
    
    low = min(Piles)
    
    high = max(Piles)
    
    bananas = 1
    
    while low <= high:
        
        mid = (low + high // 2)
        
        hours = count_hours(Piles, mid)
        
        if hours <= mid:
            
            bananas = mid
            
            high = mid - 1
        
        else:
            
            low = mid + 1
            
        return bananas
    
    return -1




# Main/Driver code:

piles = [7, 15, 6, 3]

hour = 8

answer = min_no_of_bananas(piles, hour)


if answer == -1:

    print(f"Koko cannot be able to eat in {hour} hours !")

else:
    
    print(f" Koko can eat in {answer} bananas in {hour} hours.")
    
    
                   
            