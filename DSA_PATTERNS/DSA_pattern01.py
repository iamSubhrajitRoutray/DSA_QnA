'''Rectangular Star Pattern'''

class Solution:
    def pattern1(self, n):
        
        #the outer loop is for the rows->
        for i in range(n):
            
            #the inner loop for the columns->
            for j in range(n):
                print('*',end=' ')
                
            # Move to the next line after printing the current row
            print()
            
            
class Solution:
    
    def pattern1(self, n):
    
        for i in range(n):
            
            print('*' * n)


# Main/Driver code :          
obj = Solution()
n = 5
obj.pattern1(n)