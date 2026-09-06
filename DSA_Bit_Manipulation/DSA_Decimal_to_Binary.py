'''Convert a Decimal Number to Binary Form'''

def decimal_to_binary(num: int)->str:
    
    result = " "
    
    while num > 0:
        
        if num % 2 == 1:
        
            result += "1"
        
        else:
        
            result += "0"

        num = num // 2
        
    result = result[::-1]
    
    return result


# MAIN/DRIVER CODE:

number = 13

answer = decimal_to_binary(number)

print(f"\nThe binary form of {number} is : {answer}\n")
    