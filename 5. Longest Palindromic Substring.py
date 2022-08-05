# Given a string s, return the longest palindromic substring in s.
###############################################################
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Input: s = "cbbd"
# Output: "bb"
###############################################################

# approach 1
# reference: https://www.youtube.com/watch?v=XYQecbcd6_c
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
def longestPalindrome(s):
    temp = ""
    templen = 0
    for i in range(len(s)):
        # odd len
        l, r = i, i
        while l >=0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > templen:
                temp = s[l:r+1]
                templen = r - l + 1
            l -= 1
            r +=1
        # odd len
        l, r = i, i+1
        while l >=0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > templen:
                temp = s[l:r+1]
                templen = r - l + 1
            l -= 1
            r += 1
    return temp

## Driver code
if __name__=='__main__':
    s = "babad"
    print(longestPalindrome(s))