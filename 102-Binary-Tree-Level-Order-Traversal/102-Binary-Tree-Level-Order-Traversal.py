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




#------------------
# This is another solution 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        queue = [root]
        answers = []
        while len(queue) > 0:
            answer = []
            l = len(queue)
            for i in range(l):
                pop = queue.pop(0)
                answer.append(pop.val)
                if pop.left is not None:
                    queue.append(pop.left)
                if pop.right is not None:
                    queue.append(pop.right)
            answers.append(answer)
        print(answers)
        return answers