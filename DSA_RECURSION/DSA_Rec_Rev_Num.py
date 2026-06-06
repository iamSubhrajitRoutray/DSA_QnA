'''Print N to 1 using Recursion'''

def reverse_num(num, n):
    
    if num > n:
        
        return
    
    reverse_num(num + 1, n)
    
    print(num)
    
    
# Main/Driver code :
val = int(input('Enter the number: '))

print(f'Descending order {val} : ')

rev_rec = reverse_num(1, val)
