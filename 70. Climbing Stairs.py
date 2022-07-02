# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?
###############################################################
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
###############################################################

# approach 1 (dp)
# reference: https://www.youtube.com/watch?v=Y0lT9Fck7qI
# class Solution:
#     def climbStairs(self, n: int) -> int:
def climbStairs(n):
    m, m_1 = 1, 1
    for i in range(n-1):
        temp = m
        m += m_1
        m_1 = temp
    return m

## Driver code
if __name__=='__main__':
    n = 2
    print(climbStairs(n))