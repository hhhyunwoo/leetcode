from typing import List

class Solution:
    def dfs(self, node):
        if self.visited[node] == -1:
            return True
        elif self.visited[node] == 1:
            return False

        self.visited[node] = -1
        for nextNode in self.graph[node]:
            if self.dfs(nextNode):
                return True
        self.visited[node] = 1

        return False 

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = {i:[] for i in range(numCourses)}
        for prerequisite in prerequisites:
            self.graph[prerequisite[0]].append(prerequisite[1])
        
        self.visited = [0 for _ in range(numCourses)]
        for node in range(numCourses):
            if self.dfs(node):
                return False
      
        return True
    
sol = Solution()
print(sol.canFinish(5,[[0,1],[0,2],[1,3],[1,4],[3,4]]))