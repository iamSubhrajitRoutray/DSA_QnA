'''Right-Angled Number Pyramid - II'''

class Solution:
    
    def pattern4(self, n):
        
        # The outer loop is for the rows.
        for i in range(n):
            
            # The inner loop for the columns.

            for j in range(i + 1):
                            
                # Print numbers from 1 to i+1.
                print(i + 1, end=' ')
                
            # Move to the next line after printing the current row.
            print()

# Main/Driver code :            
obj = Solution()

n = 3

obj.pattern4(n)