"""* Coin Change

You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
* """
class CoinChange(object):
    def coinsneeded(self, coins, amount):
        amax = amount+1
        dp = [0] +[amount+1]*amount
        for i in range(1, amount+1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]]+1)
        if dp[amount] > amount:
            return -1
        else:
            return dp[amount]

cc = CoinChange()
print(cc.coinsneeded([1, 2, 5], 11))
print(cc.coinsneeded([2], 3))
