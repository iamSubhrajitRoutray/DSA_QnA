'''Right-Angled Number Pyramid - II'''

class Solution:
    def pattern4(self, n):
        
        #the outer loop is for the rows->
        for i in range(n):
            
            #the inner loop for the columns->:
            #print numbers from 1 to i+1...
            for j in range(i+1):
                print(i+1, end=' ')
                
            # Move to the next line after printing the current row
            print()

#line of codes to run the above pseudo...               
obj = Solution()
n = 3
obj.pattern4(n)