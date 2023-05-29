from math import sqrt

class Solution:
    def isHappy(self, n: int) -> bool:
        numList = []
        numBefore = []
        flag = False
        while 1:
            numBefore.append(n)
            numList = list(map(int, str(n)))
            summation = 0
            for num in numList:
                summation += num ** 2
            if summation == 1:
                flag = True
                break
            else:
                n = summation
            
            if summation in numBefore:
                break
            
        return flag

sol = Solution()
print(sol.isHappy(19))