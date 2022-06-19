# Given an integer array nums, 
# find a contiguous non-empty subarray within the array 
# that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
# A subarray is a contiguous subsequence of the array.
###############################################################
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
###############################################################

# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
def maxProduct(nums):
    mpro = max(nums)
    cmax = cmin = 1
    for n in nums:            
        if n < 0:
            cmax, cmin = cmin, cmax
        cmax = max(n*cmax, n)
        cmin = min(n*cmin, n)
        mpro = max(mpro, cmax)
    return mpro
        

## Driver code
if __name__=='__main__':
	nums = [2,3,-2,4]
	print(maxProduct(nums))