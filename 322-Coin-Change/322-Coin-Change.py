from typing import List
from math import inf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        dp = [-1 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                maxValue = inf
                if i-coin >= 0 and dp[i-coin] != -1:
                    if dp[i] == -1:
                        dp[i] = min(maxValue, dp[i-coin] + 1) 
                    else:
                        dp[i] = min(maxValue, dp[i], dp[i-coin] + 1) 
        return dp[amount]
    

solution = Solution()
print(solution.coinChange([1,2,5], 11))