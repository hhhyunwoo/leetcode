# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = []
        maxCount = 0
        
        def dfs(node, countVal):
            nonlocal maxCount
            if node is not None:
                dfs(node.left, countVal + 1)
                if countVal > maxCount: 
                    maxCount = countVal 
                ans.append(node.val) 
                dfs(node.right, countVal + 1)

        dfs(root, 1)
        return maxCount