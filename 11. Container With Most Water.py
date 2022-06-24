# You are given an integer array height of length n. 
# There are n vertical lines drawn such that 
# the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, 
# such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
###############################################################
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.

# Input: height = [1,1]
# Output: 1
###############################################################

# approach 1 (two pointer, O(n))
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
def maxArea(height):
    result = 0
    l, r = 0, len(height) - 1
    while l < r:
        amount = (r-l) * min(height[l], height[r])
        result = max(result, amount)
        if height[l] >= height[r]:
            r -= 1
        else:
            l += 1                    
    return result

# approach 2 (O(n^2))
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
# def maxArea(height):
#         result = 0
#         for i in range(len(height)): #left pointer
#             for j in range(i+1, len(height)): # right pointer
#                 amount = (j-i) * min(height[j], height[i])
#                 result = max(result, amount)
#         return result

## Driver code
if __name__=='__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))