from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = {0:nums[0]}
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        
        return max(list(dp.values()))


solution = Solution()
print(solution.maxSubArray([-2,1]))