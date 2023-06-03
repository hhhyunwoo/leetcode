from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.graph = {i:[] for i in range(numCourses)}
        
        for a, b in prerequisites:
            self.graph[a].append(b)

        self.visited = [0 for _ in range(numCourses)]
        self.answer = []
        for node in range(numCourses):
            if self.hasCycle(node):
                return [] 

        return self.answer
    
    def hasCycle(self, node):
        if self.visited[node] == -1:
            return True
        elif self.visited[node] == 1:
            return False


        self.visited[node] = -1
        for nextNode in self.graph[node]:
            if self.hasCycle(nextNode):
                return True
        self.visited[node] = 1
        self.answer.append(node)

        return False


sol = Solution()
print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))