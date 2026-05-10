'''Number Crown Pattern'''

class Solution:
    def pattern12(self, n):
        
        # Initial number of spaces in the first row
        space = 2 * n - 1
        
        # Outer loop for the number of rows
        for i in range(1, n + 1):
            
            # Inner loop to print numbers in increasing order
            for j in range(1, i + 1):
                print(j, end=' ')
                
            # Inner loop to print spaces in the middle
            for j in range(1, space + 1):
                print(' ', end=' ')
                
            # Inner loop to print numbers in decreasing order
            for j in range(i, 0, -1):
                print(j, end=' ')
            
            # Move to the next line after printing the row    
            print()
            # Decrease spaces by 2 after each row   
            space -= 2
                     
            
#line of codes to run the above pseudo...            
obj = Solution()
n = 4
obj.pattern12(n)