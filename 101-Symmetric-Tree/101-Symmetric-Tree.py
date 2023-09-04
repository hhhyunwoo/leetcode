# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def recur(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            if node1.val == node2.val:
                if recur(node1.left, node2.right) is False:
                    return False
                if recur(node1.right, node2.left) is False:
                    return False
                return True
            else:
                return False

        return recur(root.left, root.right)            