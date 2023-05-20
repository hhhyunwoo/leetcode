# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def recur(tree: TreeNode):
            if tree is None:
                return
            recur(tree.left)
            recur(tree.right)
            answer.append(tree.val)
        recur(root)
        return answer