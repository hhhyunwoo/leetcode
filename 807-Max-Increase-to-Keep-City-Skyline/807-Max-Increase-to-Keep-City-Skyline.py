from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        nMaxList, mMaxList = [], []
        
        for i in range(n):
            nMaxList.append(max(grid[i]))
        for j in range(m):
            value = 0
            for i in range(n):
                value = max(value, grid[i][j])
            mMaxList.append(value)

        answer = 0
        for i in range(n):
            for j in range(m):
                minValue = min(nMaxList[i], mMaxList[j])
                answer += minValue - grid[i][j]

        return answer

sol = Solution()
print(sol.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))