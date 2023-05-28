from typing import List 


def dfs(i,j,n,m,grid):
    if i < 0 or i >= n or j < 0 or j >= m: 
        return False
    if grid[i][j] != 0:
        return True
    
    x, y = i-1, j
    if x < 0 or x >= n or y < 0 or y >= m: 
        return False

    grid[i][j] = -1

    l = dfs(i,j-1,n,m,grid)
    r = dfs(i,j+1,n,m,grid)
    u = dfs(i-1,j,n,m,grid)
    d = dfs(i+1,j,n,m,grid)

    return l and r and u and d



class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        answer = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and dfs(i,j,n,m,grid):
                    answer += 1

        return answer 


sol = Solution()
print(sol.closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))