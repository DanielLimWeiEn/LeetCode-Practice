class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [ amount + 1 ] * ( amount + 1 )
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        
        return dp[amount] if dp[amount] != amount + 1 else -1

"""

So... Coin Change 😀, this particular infamous problem. Now how should I solve this?

1. Naive Solution.

So, what does the recurrence look like in this case?

minAmount(amount) = 1 + min(
    minAmount(amount - coins[0]), only if amount - coins[0] > 0
    minAmount(amount - coins[1]),
    ...,
    minAmount(amount - coints[len(coins) - 1])
)

Ok, so what's the base cases?

if the amount to make up is 0 -> it's impossible so we return 0 as the minimum amount.
if the amount ever goes negative -> return -1, its impossible.
if the amount is in the coins, then return 1

minAmount(11) = 1 + min(
    minAmount(11 - 5),
    minAmount(11 - 2),
    minAmount(11 - 1)
)

2. Bottom Up DP Solution

coins = [1, 2, 5]
dp = [0, 1, 12, 2, 12, 12, 5, 12, 12, 12, 12, 12]

at each dp[i], go over the coins:
1
2
5

calculate i - coin:

if i - coin < 0: do nothing as it isn't valid.
else: dp[i] = min(dp[i], 1 + dp[i - coin])
"""
