'''Convert a Binary Number to it's Decimal Form.'''


def binary_to_decimal(num: str)->int:
    
    deci_num = 0
    
    power = 0
    
    index = len(num) - 1
    
    while index >= 0:
        
        val = int(num[index]) * (2 ** power)
        
        deci_num += val
        
        power += 1
        
        index -= 1
        
    return deci_num



# MAIN/DRIVER CODE:

number = "1101"

answer = binary_to_decimal(number)

print(f"\nThe decimal form of {number} : {answer}\n")
    
    