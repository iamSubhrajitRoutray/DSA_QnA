'''Binary Number Triangle Pattern'''

class Solution:
    
    def pattern11(self, n):
        
        # The outer loop is for the row and the inner loop for the columns
        for i in range(n):
            
            # If row index is even, start with 1
            if (i % 2 == 0):
                
                start = 1
                
            else:
                start = 0
                
            # Loop to print alternative 0's and 1's
            for j in range(i + 1):
                
                print(start, end=' ')
                
                # This line below alter betwenn 1 and 0
                start = 1 - start
                
            # Move to the next line after each row
            print()

            
# Main/Driver code :            
obj = Solution()

n = 3

obj.pattern11(n)
