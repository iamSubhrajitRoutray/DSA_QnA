'''Rat in a Maze
Q)
Given a binary matrix maze[][] of size n x n containing values 0 and 1, find all possible paths for a rat to travel from the source cell (0, 0) to the destination cell (n - 1, n - 1).
The rat can move in four directions: up(U), down(D), left(L), and right(R).

1 represents an open cell through which the rat can move.
0 represents a blocked cell that cannot be traversed.
The rat can move only through open cells and cannot visit the same cell more than once in a path. Return all valid paths as strings consisting of 'U', 'D', 'L', and 'R', representing the sequence of moves taken by the rat.

Note: Return the paths in lexicographically increasing order. If no valid path exists, return an empty list.'''



# EXAMPLES

# Input: maze[][] = {{1, 0, 0, 0}, {1, 1, 0, 1}, {1, 1, 0, 0}, {0, 1, 1, 1}}
# Output: ["DDRDRR", "DRDDRR"]

# Explanation: There are two valid paths from the source cell (0, 0) to the destination cell (3, 3).


# Input: maze[][] = [[1, 0], [1, 0]]
# Output: []

# Explanation: No path exists as the destination cell (1, 1) is blocked.




def find_path(
    i: int,
    j: int,
    n: int,
    matrix: list[list[int]],
    visited: list[list[int]],
    move: str,
    result: list[str]
      
):
    
    if (i == n - 1) and (j == n - 1):
        result.append(move)
        return
    
    # DOWNWARD MOVE:
    
    if (i + 1 < n) and not visited[i + 1][j] and matrix[i + 1][j] == 1:
        
        visited[i][j] = 1 
        
        find_path(i + 1, j, n, matrix, visited, move + "D", result)
    
        visited[i][j] = 0
        
    # LEFT MOVE:
    
    if (j - 1 >= 0) and not visited[i][j - 1] and matrix[i][j - 1] == 1:
        
        visited[i][j] = 1
        
        find_path(i, j - 1, n, matrix, visited, move + "L", result)
        
        visited[i][j] = 0
        
    # RIGHT MOVE:
    
    if (j + 1 < n) and not visited[i][j + 1] and matrix[i][j + 1] == 1:
        
        visited[i][j] = 1
        
        find_path(i, j + 1, n, matrix, visited, move + "R", result)
        
        visited[i][j] = 0
        
    # UPWARD MOVE:
    
    if (i - 1 >= 0) and not visited[i - 1][j] and matrix[i - 1][j] == 1:
        
        visited[i][j] = 1
        
        find_path(i - 1, j, n, matrix, visited, move + "U", result)
    
        visited[i][j] = 0
    


def rat_maze(maze_matrix: list[list[int]]) -> list[str]:
     
    n = len(maze_matrix)
     
    visited = [[0 for _ in range(n)] for _ in range(n)]
    
    result = []
    
    if maze_matrix[0][0] == 1:
    
        find_path(0, 0, n, maze_matrix, visited, "", result)
    
    return result


# MAIN/DRIVER CODE:

maze = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]

answer = rat_maze(maze)

print(f"\n{answer}\n")

