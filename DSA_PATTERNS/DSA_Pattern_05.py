'''Inverted Right Pyramid.'''

class Solution:
    
    def pattern5(self, n):
        
        # The outer loop is for the rows.
        for i in range(n):
            
            # The inner loop for the columns->
            # Print numbers from 0 to (n-i).
            
            for j in range(n - i):
            
                print('*', end=' ')
                
            # Move to the next line after printing the current row
            print()
            
# Main/Driver code :  
obj = Solution()
n = 3
obj.pattern5(n)