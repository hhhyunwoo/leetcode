# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        answers = []
        while queue:
            answer = []
            children = []
            for i in range(len(queue)):
                if queue[i] is not None:
                    answer.append(queue[i].val)
                    children.append(queue[i].left)
                    children.append(queue[i].right)
            for _ in range(len(queue)):
                queue.pop(0)
            queue = children
            if len(queue) == 0:
                break
            answers.append(answer)
        return answers