from typing import List

def searchDfs(x,y,n,m,grid):
    if x < 0 or y < 0 or x >= n or y >= m or grid[x][y] != "1":
        return
    grid[x][y] = "-1" 

    searchDfs(x-1,y,n,m,grid)
    searchDfs(x,y-1,n,m,grid)
    searchDfs(x+1,y,n,m,grid)
    searchDfs(x,y+1,n,m,grid)
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    searchDfs(i,j,n,m,grid)
                    count += 1
        return count 

sol = Solution()
print(sol.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))