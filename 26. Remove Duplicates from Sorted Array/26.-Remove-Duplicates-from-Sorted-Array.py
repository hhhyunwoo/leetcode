from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numDict = {}
        numAns, numDup = [], []
        for i in range(len(nums)):
            if nums[i] in numDict:
                nums[i] = -101
            else:
                numDict[nums[i]] = 0
        for i in range(len(nums)):
            if nums[i] == -101:
                numDup.append(nums[i])
            else:
                numAns.append(nums[i])
        numAns = numAns + numDup
        for i in range(len(nums)):
            nums[i] = numAns[i]
        return len(list(numDict.keys()))
    
solution = Solution()
print(solution.removeDuplicates([-1,0,0,0,0,3,3]))

