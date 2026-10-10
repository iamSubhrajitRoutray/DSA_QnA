'''Increasing Number Triangle Pattern.'''

class Solution():
    
    # Function to print the pattern of number
    def pattern13(self, n):
        
        num = 1   # Starting number
        
        # Outer loop for the number of rows
        for i in range(1, n + 1):
            
            # Inner loop to print numbers increasing by 1 in each row
            for j in range(1, i + 1):
                
                print(num, end=' ')  # Print the current number followed by a space
                
                num += 1    # Increment the number for the next print
                
            # Move to the next line after printing the current row
            print()


# Main/Driver code :            
obj = Solution()

n = 5

obj.pattern13(n)