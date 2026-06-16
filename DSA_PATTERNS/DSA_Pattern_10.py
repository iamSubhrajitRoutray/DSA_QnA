'''Half Diamond Star Pattern.'''

class Solution:
    
    # Function to print the pattern of star(*)
    def pattern10(self, n):
        
        for i in range(n):
            
            # Print stars
            print('*' * (i + 1))
    
    # Function to print the inverted pyramid
    def inverted_pattern10(self, n):
        
        # Range is initialized from '1' to avoid doubling of pattern.
        for i in range(1, n):
            
            # Print stars
            print('*' * (n - i))
  
          
# Main/Driver code :
obj = Solution()

n = 5

obj.pattern10(n)

obj.inverted_pattern10(n)