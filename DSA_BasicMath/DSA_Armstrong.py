'''Q) Check if a number is Armstrong Number or not'''

def check_armstrong(num):
    
    sum = 0
    
    p = len(str(num))
    
    while num > 0:
        
        last_digit = num % 10
        
        sum += last_digit ** p
        
        num = num // 10
    
    return sum


num = int(input('Enter the number: '))

result = check_armstrong(num)

if result == num:
    
    print(f'YES, {num} is an Armstrong Number.')

else:
    print(f'NO, {num} is not an Armstrong Number.')
            