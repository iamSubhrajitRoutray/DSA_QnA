'''Inverted Star Pyramids.'''

class Solution:
    def pattern8(self, n):
        
        # The outer loop is for the rows.
        for i in range(n):
            
            # Print leading spaces.
            for j in range(i):
                
                print(' ', end=' ')
            
            # Print star.
            for j in range(2 * n - (2 * i + 1)):
                
                print('*', end=' ')
            
            # Print trailing space.  
            for j in range(i):
                
                print(' ', end=' ')
            
            # Move to the next line after printing the current row
            print()
            

# Main/Driver code :              
obj = Solution()

n = 3

obj.pattern8(n)