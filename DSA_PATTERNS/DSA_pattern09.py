'''Diamond Star Pattern'''

class Solution:
    
    def pattern9(self, n):
        
        for i in range(n):
            
            # Print spaces before stars
            print(' ' * (n - i - 1), end=' ')
            
            # Print stars
            print('*' * (2 * i + 1), end=' ')
            
            # Print spaces after stars
            print(' ' * (n-i-1))
            
    # Function to print the inverted pyramid            
    def inverted_pattern9(self, n):
        
        for i in range(n):
            
            # Print spaces before stars
            print(' ' * i, end=' ')
            
            # Print stars
            print('*' * (2 * n - (2 * i + 1)), end=' ')
            
            # Print spaces after stars
            print(' ' * i)
            

# Main/Driver code :     
obj = Solution()

n = 5

obj.pattern9(n)

obj.inverted_pattern9(n)