'''Alpha-Ramp Pattern'''

class Solution:
    
    # Function to print the pattern where each letter is repeated in the row
    def pattern16(self, n):
        
        # Outer loop for the number of rows
        for i in range(n):
            
            # Inner loop to print the character for i times in the row
            for j in range(i+1):
                
                # Print the character followed by a space
                print(chr(65+i), end=' ')
                
            # Move to the next line after printing the current row
            print()
            
            
class Solution:
    
    # Function to print the pattern where each letter is repeated in the row
    def pattern16(self, n):
        
        # Outer loop for the number of rows
        for i in range(n):
            
            # Define the character for each row based on row index
            char = chr(65 + i)
            
            # Inner loop to print the character for i times in the row
            for j in range(i + 1):
                
                # Print the character followed by a space
                print(char, end=' ')
                
            # Move to the next line after printing the current row
            print()
            

# Main/Driver code : 
obj = Solution()

n = 5

obj.pattern16(n)