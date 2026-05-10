'''Alpha-Hill Pattern'''

class Solution:
    def pattern17(self, n):
        # Loop for each row
        for i in range(n):
            # Print leading spaces
            for j in range(n - i - 1):
                print(' ', end=' ')
                
            # Initialize character to start from 'A'
            char = ord('A')
            
            #Calculate the midpoint of the row as breakpoint = (2 * i + 1) / 2.
            breakpoint = (2 * i + 1) // 2
            
            # Print characters in row
            for j in range(1, 2 * i + 2):
                print(chr(char), end=' ')
                
                #check the pattern to be print in reverse in the same row
                if j <= breakpoint:
                    char += 1
                else:
                    char -= 1
                    
            # Move to the next line after printing the current row
            print()

# Driver code
obj = Solution()
n=4
obj.pattern17(n)