'''Star Pyramid'''

class Solution:
    def pattern7(self, n):
        
        # Outer loop is for the rows->
        for i in range(n):
            
            # Print leading spaces->
            for j in range(n - i - 1):
                print(' ', end=' ')
                
            # Print stars->  
            for j in range(2 * i + 1):
                print('*', end=' ')
                
            # Print trailing spaces-> 
            for j in range(n - i - 1):
                print(' ', end=' ')
                
            # Move to the next line after printing the current row
            print()


#line of codes to run the above pseudo...               
obj = Solution()
n = 3
obj.pattern7(n)