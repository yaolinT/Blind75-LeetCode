# Given an integer array nums, 
# return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence 
# that can be derived from an array by deleting some 
# or no elements without changing the order of the remaining elements. 
# For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
###############################################################
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
###############################################################

# approcah 1 (DP, O(n^2))
# reference: https://www.youtube.com/watch?v=cjWnW0hdF1Y&t=306s
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
def lengthOfLIS(nums):
    lis = [1] * len(nums)
    for i in range(len(nums) -1, -1, -1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                lis[i]=max(lis[i], 1+lis[j])
    return max(lis)

## Driver code
if __name__=='__main__':
    nums = [10,9,2,5,3,7,101,18]
    print(lengthOfLIS(nums))
