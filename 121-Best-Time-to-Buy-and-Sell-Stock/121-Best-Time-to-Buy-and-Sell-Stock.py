from typing import List 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPriceToBuy = 100000
        profit = 0

        for price in prices:
            if minPriceToBuy > price:
                minPriceToBuy = price

            if price-minPriceToBuy > profit:
                profit = price - minPriceToBuy
            
        return profit

solution = Solution()
print(solution.maxProfit([2,1,4]))