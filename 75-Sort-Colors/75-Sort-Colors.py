from typing import List
from math import inf

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            minimun = nums[i] 
            flag = i+1
            for j in range(i+1, len(nums)):
                if minimun > nums[j]:
                    flag = j 
                    minimun = nums[j]
            if flag < len(nums) and minimun < nums[i]:
                tmp = nums[flag]
                nums[flag] = nums[i]
                nums[i] = tmp
        print(nums)

sol = Solution()
print(sol.sortColors([0,1]))