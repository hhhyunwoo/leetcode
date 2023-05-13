from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        elif nums[0] == 0:
            return False
        dp = [-1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(nums[i]):
                if i+j < len(nums):
                    dp[i+j] += 1
            if i + nums[i] >= len(nums)-1:
                return True
            if dp[i] == -1: 
                return False
        return False


solution = Solution()
print(solution.canJump([3,2,1,0,4]))