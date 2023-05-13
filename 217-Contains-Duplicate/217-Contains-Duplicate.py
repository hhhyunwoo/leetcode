from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numDict = {}
        for num in nums:
            if num not in numDict:
                numDict[num] = 1
            else:
                return True
        return False
    

solution = Solution()
print(solution.containsDuplicate([1,2,3,1]))