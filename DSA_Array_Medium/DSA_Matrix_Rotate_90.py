'''Rotate Image by 90 degree
Q)
Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise.
The rotation must be done in place, meaning the input 2D matrix must be modified directly..'''



''' OPTIMAL APPROACH -> '''

def rotate_90(matrix):
    
    n = len(matrix)
    
    # Create a matrix of (n x n) with [0] value.
    result = [[0] * n for _ in range(n)]
    
    # Loop to print matrix
    for i in range(0, n):
        
        for j in range(0, n):
            
            # Place the (i,j) element at (j,n-1-i) in rseult matrix.
            result[j][n - 1 - i] = matrix[i][j]
    
    print(result)


# Driver/Main code -> 
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate_90(matrix)


''' OPTIMAL APPORACH -> '''

def rotate(matrix):
    
    n = len(matrix)
    
    # Loop for transpose of the matrix
    for i in range(0, n):
    
        for j in range(i+1, n):
            
            # Swap the element of (i,j) with (j,i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Loop to reverse the row
    for i in range(n):
        matrix.reverse()
    
    # Print the resultant matrix.
    print(matrix)


# Driver/Main code -> 
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate_90(matrix)

