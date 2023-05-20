# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        queue = [root]
        answers = []
        while len(queue) > 0:
            answer = []
            l = len(queue)
            for l in range(l):
                pop = queue.pop(0)
                answer.append(pop.val)
                if pop.left is not None:
                    queue.append(pop.left)
                if pop.right is not None:
                    queue.append(pop.right)
            answers.append(answer)
        return list(reversed(answers))