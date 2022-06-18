# Given an integer array nums, 
# return true if any value appears at least twice in the array, 
# and return false if every element is distinct.
###############################################################
# Input: nums = [1,2,3,1]
# Output: true

# Input: nums = [1,2,3,4]
# Output: false

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
###############################################################

# approach 1 (applying function "set()")
def containsDuplicate(nums):    
    return (len(set(nums)) != len(nums))

#### Explain ####
# set() method is used to convert any of the iterable to sequence of iterable elements with distinct elements, commonly called Set.
 
# def containsDuplicate(nums):    
#     s = set(nums)
#     if len(s) != len(nums):
#         return True
#     else:
#         return False
####

# approach 2 (other possible solution)
# def containsDuplicate(nums):    
#     for i in range(0, len(nums)):
#         for j in range(i+1,len(nums)) :
#             if nums[i] == nums[j]:
#                 return True
#     return False 

# approach 3 (possible solution using two pointers)
# def containsDuplicate(nums):    
#     l = 0
#     r = 1
#     while l < len(nums)-1:
#         if nums[l] == nums[r]:
#             return True
#         else:
#             r += 1
#             if r == len(nums):
#                 l += 1        
#     return False

## Driver code
if __name__=='__main__':
	nums = [1,2,3,1]
	print(containsDuplicate(nums))