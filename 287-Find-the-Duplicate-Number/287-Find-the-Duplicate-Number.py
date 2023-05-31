from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise, hare = 0,0

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
                
        tortoise = 0
        while True:
            tortoise = nums[tortoise]
            hare = nums[hare]
            if tortoise == hare:
                return tortoise

sol = Solution()
print(sol.findDuplicate([1,3,4,2,2]))        



###############
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numDict = {}
        for num in nums:
            if num in numDict.keys():
                return num
            else:
                numDict[num] = 1