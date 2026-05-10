'''Reverse Letter Triangle Pattern'''

class Solution:
    
    # Function to print the pattern of alphabets
    def pattern15(self, n):
        
        # Outer loop for the number of rows
        for i in range(n):
            
            # Inner loop to print alphabets from A to A + i
            for j in range(n - i):
                
                # Print the alphabet character followed by a space
                # chr(number) converts a number → corresponding ASCII character
                print(chr(65 + j), end=' ')
                
            # Move to the next line after printing the current row
            print()
            

#code for running the above pseudo...
obj = Solution()
n = 4
obj.pattern15(n)