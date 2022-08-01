# Given an unsorted array of integers nums, 
# return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
###############################################################
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence 
# is [1, 2, 3, 4]. Therefore its length is 4.

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
###############################################################

# approach 1(O(n))
# reference: https://www.youtube.com/watch?v=P6RZZMu_maU
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
def longestConsecutive(nums):
    vset, longest = set(nums), 0
    for i in nums:
        if (i-1) not in vset:
            length  = 0
            while (i + length) in vset:
                length += 1
            longest = max(length, longest)
    return longest

# approach 2(sorting)

## Driver code
if __name__=='__main__':
	nums = [100,4,200,1,3,2]
	print(longestConsecutive(nums))