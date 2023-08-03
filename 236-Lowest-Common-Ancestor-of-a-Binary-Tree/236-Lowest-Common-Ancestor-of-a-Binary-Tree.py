from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val <= root.val and q.val >= root.val:
                return root.val
            elif p.val > root.val:
                root = root.right
            elif q.val < root.val:
                root = root.left
        return TreeNode()


sol = Solution()
print(sol.lowestCommonAncestor([3,2,1,5,6,4], 2))