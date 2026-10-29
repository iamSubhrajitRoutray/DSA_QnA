'''Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.'''

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3

# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.


# Example 2:

# Input: s = "bbbbb"
# Output: 1

# Explanation: The answer is "b", with the length of 1.


# Example 3:

# Input: s = "pwwkew"
# Output: 3

# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 105
# s consists of English letters, digits, symbols and spaces.



'''BRUTE-FORCE APPROACH'''


def substring(string):
    
    max_i = 0
    
    for i in range(len(string)):
        
        my_set = set()
        
        for j in range(i, len(string)):
            
            if string[j] in my_set:
                break
            
            max_i = max(max_i, (j - i + 1))

            my_set.add(string[j])
    
    return max_i



# MAIN/DRIVER CODE: 

s = "pwwkew"

answer = substring(s)

print(f"\nLongest Substring in given string '{s}' : {answer}\n")







'''OPTIMAL APPROACH '''
# USING SLIDING WINDOW 



def longest_substring(string):
    
    left, right = 0, 0
    
    my_dict = dict()
    
    max_s = 0
    
    while right < len(string):
        
        if string[right] in my_dict:
            
            left = max(left, (my_dict[string[right]] + 1))
            
        my_dict[string[right]] = right
        
        max_s = max(max_s, (right - left + 1))
        
        right += 1
    
    return max_s


# MAIN/DRIVER CODE: 

s = "abcabcbb"

answer = longest_substring(s)

print(f"\nLongest Substring in given string '{s}' : {answer}\n")

