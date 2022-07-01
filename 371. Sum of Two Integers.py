# Given two integers a and b, 
# return the sum of the two integers without using the operators + and -.
###############################################################
# Input: a = 1, b = 2
# Output: 3

# Input: a = 2, b = 3
# Output: 5
###############################################################

#approach 1 (using sum())
# class Solution:
#     def getSum(self, a: int, b: int) -> int:
# def getSum(a, b):
#     return sum([a, b])

#approach 2 (working but exceeded time limit)
# class Solution:
#     def getSum(self, a: int, b: int) -> int:
# def getSum(a, b):
#     s = 0
#     while b != 0:
#         s = (a & b) << 1
#         a = a ^ b
#         b = s
#     return a

#approach 3 (optimized from approach 2)
# class Solution:
#     def getSum(self, a: int, b: int) -> int:
def getSum(a, b):
    mask = 0xffffffff
    sum = (a ^ b) & mask
    carry = a & b
    while carry!=0:
        a = sum
        b = (carry << 1) & mask
        sum = (a ^ b) & mask
        carry = a & b
    if sum & 0x80000000:
        sum -= 0x100000000
    return sum

## Driver code
if __name__=='__main__':
	a , b = 1, 2
	print(getSum(a, b))

    
        