# You are given an integer array coins representing coins of different denominations 
# and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.
###############################################################
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Input: coins = [2], amount = 3
# Output: -1

# Input: coins = [1], amount = 0
# Output: 0
###############################################################

# approach 1 (dp)
# reference: https://www.youtube.com/watch?v=H9bfqozjoqs
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
def coinChange(coins, amount):
    dp = [amount+1] * (amount+1)
    dp[0] = 0
    for i in range (1, amount+1):
        for j in coins:
            if i-j >= 0:
                dp[i]=min(dp[i], 1+dp[i-j])
    return dp[amount] if dp[amount] != amount+1 else -1

## Driver code
if __name__=='__main__':
	coins, amount = [1,2,5], 11
	print(coinChange(coins, amount))