class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def recur(tree: TreeNode):
            if tree is None:
                return
            recur(tree.left)
            answer.append(tree.val)
            recur(tree.right)
        recur(root)
        return answer