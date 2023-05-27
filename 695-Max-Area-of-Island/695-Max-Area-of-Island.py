from typing import List

count = 0

def dfs(x,y,n,m,grid):
    global count 
    if x < 0 or y < 0 or x >= n or y >= m or grid[x][y] != 1:
        return 
    grid[x][y] = -1
    count += 1
    dfs(x-1,y,n,m,grid)
    dfs(x,y-1,n,m,grid)
    dfs(x+1,y,n,m,grid)
    dfs(x,y+1,n,m,grid)

    return count


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        answer = 0
        global count
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count = 0
                    dfsAns = dfs(i,j,n,m,grid)
                    if answer < dfsAns:
                        answer = dfsAns
        return answer 
    

sol = Solution()
print(sol.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))