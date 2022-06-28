# Given an integer n, 
# return an array ans of length n + 1 such that for each i (0 <= i <= n), 
# ans[i] is the number of 1's in the binary representation of i.
###############################################################
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
###############################################################

#approach 1 (bit sum)
# class Solution:
#     def countBits(self, n: int) -> List[int]:
def countBits(n):
        a = [0]
        for i in range(1, n+1):
            a.append(bin(i).count("1"))
        return a

#approach 2 (XOR)
# def countBits(n):
#     results = [0] 
#     for i in range(1, n+1):
#         results.append(results[i & (i-1)] + 1)   
#     return results

## Driver code
if __name__=='__main__':
	n = 5
	print(countBits(n))