# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        queue = [root]
        answers = []
        idx = 1
        while len(queue) > 0:
            answer = []
            l = len(queue)
            for i in range(l):
                pop = queue.pop(0)
                answer.append(pop.val)
                if idx%2 == 0:
                    if pop.left is not None:
                        queue.append(pop.left)
                    if pop.right is not None:
                        queue.append(pop.right)
                else:
                    if pop.right is not None:
                        queue.append(pop.right)
                    if pop.left is not None:
                        queue.append(pop.left)
            answers.append(answer)
            idx += 1
        print(answers)
        return answers
