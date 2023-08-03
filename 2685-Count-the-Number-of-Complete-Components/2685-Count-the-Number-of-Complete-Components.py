#from typing import List
#
#class Solution:
#    def dfs(self, node):
#        if self.visited[node] == 1:
#            return False
#        elif self.visited[node] == -1:
#            return True
#        
#        self.visited[node] = -1
#
#        for nextNode in self.graph[node]:
#            if self.dfs(nextNode):
#                return True
#        
#        self.visited[node] = 2
#        return False
#
#    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
#        self.graph = {i:[] for i in range (n)}
#        for edge in edges:
#            self.graph[edge[0]].append(edge[1])
#        print(self.graph)
#        self.visited = [0 for _ in range(n)]
#
#        cycleCount = 0
#        for node in range(n):
#            if self.visited[node] != 2 and self.dfs(node) is True:
#                cycleCount += 1
#
#        print(cycleCount)
#
#        return cycleCount


from typing import List

def dfs(visited, course, graph):
    if visited[course] == 1:
        return False
    elif visited[course] == -1:
        return True

    visited[course] = -1

    for nextCourse in graph[course]:
        if dfs(visited, nextCourse,graph):
            return True

    visited[course] = 1
    return False


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        if len(edges) == 0: return True

        graph = {i:[] for i in range(n)}
        for req in edges:
            graph[req[0]].append(req[1])
        print(graph)

        visited = [0 for _ in range(n)]

        cycleCounter = 0
        for course in range(n):
            if dfs(visited, course,graph):
                cycleCounter += 1 
        print(cycleCounter)

        return True
    
sol = Solution()
print(sol.countCompleteComponents(6,[[0,1],[0,2],[1,2],[3,4]]))