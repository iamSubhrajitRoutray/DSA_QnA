'''Inverted Star Pyramids'''

class Solution:
    def pattern8(self, n):
        
        #the outer loop is for the rows->
        for i in range(n):
            
            #print leading spaces->
            for j in range(i):
                print(' ', end=' ')
            
            #print stars->    
            for j in range(2 * n - (2 * i + 1)):
                print('*', end=' ')
            
            #print trailing spaces->    
            for j in range(i):
                print(' ', end=' ')
            
            # Move to the next line after printing the current row
            print()
            

#line of codes to run the above pseudo...               
obj = Solution()
n = 3
obj.pattern8(n)