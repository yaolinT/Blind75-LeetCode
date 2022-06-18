# Given an integer array nums, 
# return an array answer such that answer[i] 
# is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums 
# is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time 
# and without using the division operation.
###############################################################
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
###############################################################

# approach 1 (weird mult method, O(n))
# rederence: https://www.youtube.com/watch?v=bNvIQI2wAjk
def productExceptSelf(nums):
    out = [1]*len(nums)
    l2r = 1 # left to right
    for i in range(len(nums)):
        out[i] = l2r
        l2r    = l2r * nums[i]
    r2l = 1 # right to left
    for j in range(len(nums)-1, -1, -1):
        out[j] = out[j]  * r2l
        r2l    = nums[j] * r2l
    return out

# approach 2 (type float, probably not in O(n))
# def productExceptSelf(nums):
#     x = 1
#     y = []
#     for i in range(len(nums)):
#         x = x * nums[i]
#     for j in range(len(nums)):
#         y.append(x/nums[j])
#     return y

## Driver code
if __name__=='__main__':
	nums = [1,2,3,4]
	print(productExceptSelf(nums))