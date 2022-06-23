# Given an integer array nums, 
# return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, 
# and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
###############################################################
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Input: nums = []
# Output: []

# Input: nums = [0]
# Output: []
###############################################################

#approach 1 (Time: O(nlogn)+[O(n^2)]; Memory: O(1)～O(n))
#reference: https://www.youtube.com/watch?v=jzZsG8n2R9A
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
def threeSum(nums):
    result = []
    nums.sort()
    
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            threeS = a + nums[l] + nums[r]
            if threeS > 0:
                r = r - 1
            elif threeS < 0:
                l = l + 1
            else:
                result.append([a, nums[l], nums[r]])
                l = l + 1
                while nums[l] == nums[l - 1] and l < r:
                    l = l + 1
    return result

## Driver code
if __name__=='__main__':
	nums = [-1,0,1,2,-1,-4]
	print(threeSum(nums))