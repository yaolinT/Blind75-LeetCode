# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed. 
# All houses at this place are arranged in a circle. 
# That means the first house is the neighbor of the last one. 
# Meanwhile, adjacent houses have a security system connected, 
# and it will automatically contact the police 
# if two adjacent houses were broken into on the same night.
# Given an integer array nums 
# representing the amount of money of each house, 
# return the maximum amount of money 
# you can rob tonight without alerting the police.
###############################################################
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Input: nums = [1,2,3]
# Output: 3
###############################################################

# approach 1 (DP)
# reference: https://www.youtube.com/watch?v=rWAJCfYYOvM
# class Solution:
#     def rob(self, nums: List[int]) -> int:
def rob(nums):
    return max(nums[0], rob1(nums[1:]), rob1(nums[:-1]))
def rob1(nums):
    l, r = 0, 0
    for i in nums:
        res = max(l + i, r)
        l = r
        r = res
    return r

## Driver code
if __name__=='__main__':
	nums = [2,3,2]
	print(rob(nums))