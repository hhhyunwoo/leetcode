from typing import List

def dfs(x,y,n,m,grid1,grid2):
    if x < 0 or y < 0 or x >= n or y >= m or grid2[x][y] == 0:
        return
    
    grid2[x][y] = 0

    dfs(x-1,y,n,m,grid1,grid2)
    dfs(x,y-1,n,m,grid1,grid2)
    dfs(x+1,y,n,m,grid1,grid2)
    dfs(x,y+1,n,m,grid1,grid2)

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n, m = len(grid1), len(grid1[0])
        answer = 0
        
        for i in range(n):
           for j in range(m):
               if grid2[i][j] == 1 and grid1[i][j] == 0:
                   dfs(i,j,n,m,grid1,grid2)
        
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1:
                    dfs(i,j,n,m,grid1,grid2)
                    answer += 1
        return answer
    
sol = Solution()
print(sol.countSubIslands([[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]))