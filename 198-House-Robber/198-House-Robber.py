from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = {0: nums[0], 1: nums[1]}
        dp[2] = max(dp[0] + nums[2], dp[1])
        for i in range(3, len(nums)):
            dp[i] = max(dp[i-3] + nums[i], dp[i-2] + nums[i], dp[i-1])

        return max(list(dp.values()))


solution = Solution()
print(solution.rob([2,1,1,2]))