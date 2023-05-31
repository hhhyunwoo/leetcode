from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsDict = {}
        for i in range(len(nums)+1):
            numsDict[i] = 0
        print(numsDict)
        
        for num in numsDict.keys():
            if num not in nums:
                return num



sol = Solution()
print(sol.missingNumber([3,0,1]))