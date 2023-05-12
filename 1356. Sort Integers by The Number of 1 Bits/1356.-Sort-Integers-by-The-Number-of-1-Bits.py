from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def decimal2Binary(num):
            binaryVal = []
            while True :
                q = int(num / 2)
                r = int(num % 2)
                num = q
                binaryVal.insert(0, r)
                if num == 0:
                    break
            return binaryVal
        
        arrBinDict = {}
        for num in arr:
            arrBinDict[num] = decimal2Binary(num)


        ansDict = {}
        for num in arr:
            counterOne = arrBinDict[num].count(1)
            if counterOne in ansDict:
                ansDict[counterOne].append(num)
            else:
                ansDict[counterOne] = [num]

        ans = []
        for i in sorted(list(ansDict.keys())):
            ans = ans + sorted(ansDict[i])

        return ans

solution = Solution()
print(solution.sortByBits([10,100,1000,10000]))