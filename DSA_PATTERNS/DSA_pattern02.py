'''Right-Angled Triangle Pattern'''

class Solution:
    def pattern2(self, n):
        
        #the outer loop is for the rows->
        for i in range(n):
            
            #the inner loop for the columns->
            for j in range(i + 1):
                print('*', end=' ')
                
            # Move to the next line after printing the current row
            print()
            
            
'''class Solution:
    def pattern2(self, n):
        for i in range(n):
            print('*'*(i+1))'''

# Driver code
obj = Solution()
n = 4
obj.pattern2(n)
