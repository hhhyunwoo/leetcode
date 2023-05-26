
from typing import List

def search(x,y,n,m,grid):
    ans = 0
    if x < 0 or y < 0 or x >=n or y>=m: 
        ans +=1
    elif grid[x][y] == 0:
        ans += 1
    return ans

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        answer = 0 
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    answer += search(i-1,j,n,m,grid)
                    answer += search(i,j-1,n,m,grid)
                    answer += search(i+1,j,n,m,grid)
                    answer += search(i,j+1,n,m,grid)
        return answer 

sol = Solution()
print(sol.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))