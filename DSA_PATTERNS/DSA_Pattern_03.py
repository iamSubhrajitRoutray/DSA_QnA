'''Right-Angled Number Pyramid.'''

class Solution:
    
    def pattern3(self, n):
        
        # The outer loop is for the rows->
        for i in range(n):
            
            # the inner loop for the columns->
            for j in range(i + 1):
                print(j + 1, end=' ')  # Print numbers from (j+1) to (i+1)...
                
            # Move to the next line after printing the current row
            print()
            
            
# Main/Driver code :           
obj = Solution()

n = 3

obj.pattern3(n)