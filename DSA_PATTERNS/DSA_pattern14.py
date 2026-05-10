'''Increasing Letter Triangle Pattern'''

class Selection:
    
    # Function to print the pattern of alphabets
    def pattern14(self, n):
        
        # Outer loop for the number of rows
        for i in range(n):
            
            # Inner loop to print alphabets from A to A + i
            for j in range(i+1):
                
                # Print the alphabet character followed by a space
                # chr(number) converts a number → corresponding ASCII character
                print(chr(65+j), end=' ')
                
                # ord('A') → returns ASCII value of 'A' (65)
                '''print(chr(ord('A'+j), end=' '))''' 
                   
            # Move to the next line after printing the current row
            print()
        
        
#code for running the above pseudo...
obj = Selection()
n = 4
obj.pattern14(n)

        