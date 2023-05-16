from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        changeVal = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    changeVal.append([i,j])
        for val in changeVal:
            for i in range(m):
               matrix[i][val[1]] = 0 
            for i in range(n):
               matrix[val[0]][i] = 0 
        print(matrix)


solution = Solution()
print(solution.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))