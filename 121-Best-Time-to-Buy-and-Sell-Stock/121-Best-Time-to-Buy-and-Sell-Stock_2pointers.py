class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxPrice = 0
        while r < len(prices):
            cur = prices[r] - prices[l]
            if prices[r] < prices[l]:
                l = r
            else:
                maxPrice = max(cur, maxPrice)
            r += 1
        return maxPrice
