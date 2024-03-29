from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = {0: nums[0], 1: max(nums[0], nums[1])}

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return max(list(dp.values()))


solution = Solution()
print(solution.rob([2,1,1,2]))