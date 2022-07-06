# Given an array of distinct integers nums and a target integer target, 
# return the number of possible combinations that add up to target.
# The test cases are generated so that the answer can fit in a 32-bit integer.
###############################################################
# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.

# Input: nums = [9], target = 3
# Output: 0
###############################################################

# approach 1 (dp, with dictionary)
# class Solution:
#     def combinationSum4(self, nums: List[int], target: int) -> int:
def combinationSum4(nums, target):
    dp = {0:1} # dict, first location [0] is saved "1"
    for i in range(1, target+1):
        dp[i] = 0
        for j in nums:
            dp[i] = dp[i] + dp.get(i-j, 0)
    return dp[i]

## Driver code
if __name__=='__main__':
    nums, target = [9], 3
    print(combinationSum4(nums, target))
