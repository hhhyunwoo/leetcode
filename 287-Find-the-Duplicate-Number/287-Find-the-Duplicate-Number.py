class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numDict = {}
        for num in nums:
            if num in numDict.keys():
                return num
            else:
                numDict[num] = 1
        