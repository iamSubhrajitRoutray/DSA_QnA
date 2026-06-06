'''Inverted Numbered Right Pyramid'''

class Solution:
    
    def pattern6(self, n):
        
        # The outer loop is for the rows->
        for i in range(n):
            
            # The inner loop for the column->
            # Print number from 1 to (n+1-i)...
            for j in range(1, n - i + 1,):
                print(j, end=' ')
                
            # Move to the next line after printing the current row
            print()

# Main/Driver code :            
obj = Solution()
n=5
obj.pattern6(n)