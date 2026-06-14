'''Program to generate Pascal's Triangle
Q)
Write a program to generate Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it'''

  

def triangle(n):
    
    row = [1]
    
    result = []
    
    for _ in range(n):
    
        result.append(row)
    
        new_row = [1]
        
        for i in range(len(row) - 1):
        
            new_row.append(row[i] + row[i + 1])
        
        new_row.append(1)
        
        row = new_row
    
    return result


# Main/Driver code :
num = 4
ans = triangle(num)
print(ans)    