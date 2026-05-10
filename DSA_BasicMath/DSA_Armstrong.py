'''Check if a number is Armstrong Number or not'''

def check_armstrong(n):
    sum = 0
    p = len(str(n))
    
    while n > 0:
        l_d = n % 10
        sum += l_d ** p
        n = n // 10
    return sum


num = int(input('Enter your number: '))

result = check_armstrong(num)

if result == num:
    print(f'YES, {num} is an Armstrong Number.')
else:
    print(f'NO, {num} is not an Armstrong Number.')
            