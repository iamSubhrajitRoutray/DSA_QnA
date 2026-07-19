'''Longest Common Prefix
Q)
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".'''


def longest_common_prefix(s):
    
    result = ""
    
    base = s[0]
    
    for i in range(len(base)):
        for word in s[1 : ]:
            
            if i == len(word) or word[i] != base[i]:
                return result
            
        result = result + base[i]
        
    return result



# Main/Driver code:

words = ["flower", "flow", "flight"]

answer = longest_common_prefix(words)

print(f"Common Prefix in given List: {answer}")



# Time Complexity : O(m x n)

# Space Complexity : O(1) or O(m); where m is the lenght of the longest prefix.
        
            
    
    
    
    