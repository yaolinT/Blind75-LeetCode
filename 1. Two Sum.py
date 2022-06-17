# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.
###############################################################
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]
###############################################################

# approach 1
# class Solution:
def twoSum(nums, target):
    for i in range(len(nums)):
        a = target - nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] == a:
                return i, j

# approach 2
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            num = nums[i]+nums[j]                
            if num == target:
                return [i, j]

## Driver code
if __name__=='__main__':

	nums = [2,7,11,15]
	target = 9
	print(twoSum(nums, target))

