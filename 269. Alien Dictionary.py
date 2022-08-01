# There is a new alien language which uses the latin alphabet. 
# However, the order among letters are unknown to you. 
# You receive a list of non-empty words from the dictionary, 
# where words are sorted lexicographically 
# by the rules of this new language. 
# Derive the order of letters in this language.

# Note:
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, 
# then a must appear before b in the given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, 
# return any one of them is fine.
###############################################################
# Given the following words in dictionary,
# Input: words = ["wrt", "wrf", "er", "ett", "rftt"]
# TOutput: "wertf"

# Given the following words in dictionary,
# Input: words = ["z", "x"]
# Output: "zx"

# Given the following words in dictionary,
# Input: words = ["z", "x", "z"]
# Output: ""
# Explanation: The order is invalid, so return "".
###############################################################

# approach 1(DFS, Topological sort)
# reference: https://www.youtube.com/watch?v=6kTZYvNNyps
# Topological sort: https://en.wikipedia.org/wiki/Topological_sorting
def alienOrder(words):
    adj = {c:set() for w in words for c in w}
    for i in range(len(words)-1):
        a, b = words[i], words[i+1]
        minlen = min(len(a), len(b))
        if len(a) > len(b) and a[:minlen] == b[:minlen]:
            return ""
        for j in range(minlen):
            if a[j] != b[j]:
                adj[a[j]].add(b[j])
    vset, temp = {}, []
    def dfs(c):
        if c in vset:
            return vset[c]
        vset[c] = True
        for k in adj[c]:
            if dfs(k):
                return True
        vset[c]=False
        temp.append(c)
    for c in adj:
        if dfs(c):
            return ""
    temp.reverse()
    return "".join(temp)

## Driver code
if __name__=='__main__':
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    print(alienOrder(words))