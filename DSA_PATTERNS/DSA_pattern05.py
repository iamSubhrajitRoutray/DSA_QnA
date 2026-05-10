'''Inverted Right Pyramid'''

class Solution:
    def pattern5(self, n):
        
        #the outer loop is for the rows->
        for i in range(n):
            
            #the inner loop for the columns->
            #print numbers from 0 to (n-i)...
            for j in range(n - i):
                print('*', end=' ')
                
            # Move to the next line after printing the current row
            print()
            
#line of codes to run the above pseudo...   
obj = Solution()
n = 3
obj.pattern5(n)