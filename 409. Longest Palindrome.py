# Given a string s which consists of lowercase or uppercase letters, 
# return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
###############################################################
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
###############################################################

# approach 1
# reference: https://maxming0.github.io/2020/08/14/Longest-Palindrome/
# class Solution:
#     def longestPalindrome(self, s: str) -> int:
def longestPalindrome(s):
    import collections
    temp = exc = 0
    for i in collections.Counter(s).values():
        if i % 2 == 0:
            temp += i
        else:
            temp, exc = temp+i-1, 1
    return temp + exc

## Driver code
if __name__=='__main__':
    s = "abccccdd"
    print(longestPalindrome(s))