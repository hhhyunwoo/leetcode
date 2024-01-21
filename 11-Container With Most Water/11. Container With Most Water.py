class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxValue = 0
        while l < r:
            cur = min(height[l], height[r]) * (r-l)
            maxValue = max(maxValue, cur)
            print(l,height[l], r,height[r],maxValue)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return maxValue
