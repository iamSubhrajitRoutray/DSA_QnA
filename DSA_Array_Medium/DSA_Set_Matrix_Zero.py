''''''

''' BRUTE FORCE APPRAOCH -> '''

def infinity(matrix, row, col):
    
    r = len(matrix)
    c = len(matrix[0])
    
    for i in range(0, r):
        
        if matrix[i][col] != 0:
           
            matrix[i][col] = float('inf')
    
    for j in range(0, c):
        
        if matrix[row][j] != 0:
            
            matrix[row][j] = float('inf')


def set_zero(matrix):
    
    row = len(matrix)
    col = len(matrix[0])
    
    for i in range(0, row):
        
        for j in range(0, col):
            
            if matrix[i][j] == 0:
               
                infinity(matrix, i, j)
                
    for i in range(0, row):
       
        for j in range(0, col):
            
            if matrix[i][j]==float('inf'):
                
                matrix[i][j] = 0
    
    print(matrix)
    
    
    
matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
set_zero(matrix)



def set_zero(matrix):
    
    r = len(matrix)
    c = len(matrix[0])
    
    row = [0] * r
    col = [0] * c
    
    for i in range(0, r):

        for j in range(0, c):

            if matrix[i][j] == 0:

                row[i] = -1
                col[j] = -1
    

    for i in range(0, r):

        for j in range(0, c):

            if row[i] == -1 or col[j] == -1:

                matrix[i][j] = 0
                
    print(matrix)
    

matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

set_zero(matrix)

    