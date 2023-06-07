from typing import List

class Solution:
    def inOrder(self,node):
        if node is None:
            return
        self.inOrder(node.left)
        self.sortedArr.append(node.val)
        self.inOrder(node.right)

    def tmp(self, nums: List[int], k: int) -> int:
        self.sortedArr = []
        self.inOrder(Tree)
        return self.sortedArr[k-1]


sol = Solution()
print(sol.tmp([3,2,1,5,6,4], 2))