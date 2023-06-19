from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = {node:[] for node in range(1,n+1)}
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if isConnected[i][j] == 1:
                    graph[i+1].append(j+1)

        isVisited = [0] * (n+1)

        def dfs(node):
            for nextNode in graph[node]:
                if isVisited[nextNode] == 0:
                    isVisited[nextNode] = 1
                    dfs(nextNode)
            
        count = 0

        for node in range(1,n+1):
            print(node, isVisited)
            if isVisited[node] == 0:
                count += 1
                dfs(node)
        return count
                





sol = Solution()
print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))