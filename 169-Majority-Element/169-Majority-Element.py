class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxCount = 0
        ans = 0
        for num in set(nums):
            if maxCount < nums.count(num):
                maxCount = nums.count(num)
                ans = num
        return ans