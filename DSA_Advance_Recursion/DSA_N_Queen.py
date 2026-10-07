'''N-Queens
Q)
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.'''



'''BRUTE-FORCE APPROACH'''


def isSafe(row, column, board, num):
    
    origin_row = row
    origin_col = column
    
    while row >= 0 and column >= 0:
        
        if board[row][column] == "Q":
            return False

        row -= 1
        column -= 1
    
    row = origin_row
    column = origin_col
    
    while column >= 0:
        
        if board[row][column] == "Q":
            return False
        
        column -= 1
        
    row = origin_row
    column = origin_col
    
    while row < num and column >= 0:
        
        if board[row][column] == "Q":
            return False
        
        row += 1
        column -= 1
        
    return True




def solve(column, result, board, num):
    
    if column == num:
        result.append(board[:])
        return
    
    for row in range(num):
        
        if isSafe(row, column, board, num):
            
            board[row] = board[row][:column] + "Q" + board[row][column + 1:]
            
            solve(column + 1, result, board, num)
            
            board[row] = board[row][:column] + "." + board[row][column + 1:]



def N_Queen_Solution(num):
    
    result = []
    
    board = ["." * num for _ in range(num)]
    
    solve(0, result ,board, num)
    
    return result


# MAIN/DRIVER CODE:

numb = 4

answer = N_Queen_Solution(numb)

print(f"\nAll solution of N-Queen for N as {numb}: {answer}\n")





'''OPTIMAL APPROACH'''


def solution(column, horizontal, lower_diagonal, upper_diagonal, board, result, num):
    
    if column == num:
        result.append(board[:])
        return
    
    for row in range(num):
        
        if (
            horizontal[row] == 0 and
            lower_diagonal[row + column] == 0 and
            upper_diagonal[(num - 1) + (column - row)] == 0
        ):
            
            board[row] = board[row][:column] + "Q" + board[row][column + 1:]
           
            horizontal[row] = 1
            
            lower_diagonal[row + column] = 1
            
            upper_diagonal[(num - 1) + (column - row)] = 1
                        
            solution(column + 1, horizontal, lower_diagonal, upper_diagonal, board, result, num)
            
            board[row] = board[row][:column] + "." + board[row][column + 1:]
            
            horizontal[row] = 0
            
            lower_diagonal[row + column] = 0
            
            upper_diagonal[(num - 1) + (column - row)] = 0



def N_Queen(num):
    
    result = []
    
    board = ["." * num for _ in range(num)]
    
    horizontal = [0] * num
    

    lower_diagonal = [0] * (2 * num - 1)

    upper_diagonal = [0] * (2 * num - 1)
    
    solution(0, horizontal, lower_diagonal, upper_diagonal, board, result, num)
    
    return result



# MAIN/DRIVER CODE:

numb = 4

answer = N_Queen(numb)

print(f"\nAll solution of N-Queen for N as {numb}: {answer}\n")
