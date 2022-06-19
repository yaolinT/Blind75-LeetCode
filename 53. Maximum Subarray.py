# Given an integer array nums, 
# find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.
###############################################################
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Input: nums = [1]
# Output: 1

# Input: nums = [5,4,-1,7,8]
# Output: 23
###############################################################

#approach 1 (Kadane’s Algorithm, dynamic programming algorithm, O(n))
#reference: https://www.youtube.com/watch?v=5WZl3MMT0Eg&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=5
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
def maxSubArray(nums):
    msub = nums[0]
    csum = 0
    for n in nums:            
        if csum < 0:
            csum = 0
        csum += n
        msub = max(msub, csum)
    return msub

#approach 2 (O(n^2) or even O(n^3))

## Driver code
if __name__=='__main__':
	nums = [-2,1,-3,4,-1,2,1,-5,4]
	print(maxSubArray(nums))