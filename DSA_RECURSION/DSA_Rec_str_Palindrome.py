'''Check if the given String is Palindrome or not'''

def string_palindrome(i, s):
    
    # Base Condition: If i exceeds half of the string, all the elements have been compared
    # and the string is a palindrome, return True, or print statement as a True
    
    if i >= len(s) // 2:
    
        return print('YES, The given string is palindrome.')
    
     # If the start and end characters are not equal, it's not a palindrome, 
     # return False, or print statement as a False
     
    if s[i] != s[len(s) - i - 1]:
    
        return print('NO, The given string is not a palindrome.')
    
    # If both characters are the same, increment i and check start+1: (i) and end-1 (s)
    
    return string_palindrome(i + 1, s)

# Main / Driver code ->
word = input('Enter the word: ')
string_palindrome(0, word)
