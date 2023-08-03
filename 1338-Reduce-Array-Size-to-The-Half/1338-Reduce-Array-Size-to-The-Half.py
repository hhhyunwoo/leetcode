from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        minLen = len(arr) / 2
        arrDict = {arr[i]:0 for i in range(len(arr))}
        for i in range(len(arr)):
            arrDict[arr[i]] += 1

        sortedArrDict = [k for k,v in sorted(arrDict.items(), key=lambda item: -item[1])]
        answer = 1000000 
        if len(sortedArrDict) == 1 or (len(sortedArrDict) != 1 and len(arr) == 2):
            return 1

        for i in range(0,len(sortedArrDict)):
            size = 1
            sumRepeat = arrDict[sortedArrDict[i]]
            for j in range(len(sortedArrDict)-1, 0, -1):
                if sumRepeat >= minLen:
                    if answer > size:
                        answer = size
                    break
                size += 1
                sumRepeat += arrDict[sortedArrDict[j]]

        return answer

sol = Solution()
print(sol.minSetSize([9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]
))
