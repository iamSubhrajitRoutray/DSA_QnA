'''Print N to 1 using Recursion'''

def reverse_num(c_num, num):
    
    if c_num > num:
        return
    
    reverse_num(c_num + 1, num)
    
    print(c_num)
    
    
# Driver code ->
val = int(input('Enter the number: '))

print(f'Descending order {val} : ')

rev_rec = reverse_num(1, val)
