from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = {k: 0 for k in nums}
        for num in nums:
            numsDict[num] += 1
        sortedNumsDict = [k for k,v in sorted(numsDict.items(), key=lambda item: item[1])]
        print(sortedNumsDict) 
        answer = [] 
        for i in range(k):
            answer.append(sortedNumsDict[len(sortedNumsDict)-1-i])
        return answer
    
sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3],2))