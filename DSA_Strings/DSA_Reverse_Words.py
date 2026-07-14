'''Reverse Words in a String
Q)
Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ).
A word is defined as a sequence of non-space characters. The words in s are separated by at least one space.
Return a string with the words in reverse order, concatenated by a single space.'''




def reversal(s):
    
    words = s.split()
    words.reverse()
    
    ans = " ".join(words)

    return ans



string = "welcome to the jungle"

print(f"Given string :\n{string}\n")

result = reversal(string)

print(f"Reverse :\n{result}\n")
    
    