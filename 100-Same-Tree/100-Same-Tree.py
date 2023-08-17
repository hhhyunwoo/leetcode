# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans = []
        queue = [p]

        def bfs():
            while queue:
                node = queue.pop(-1)
                if node:
                    if node == 10001:
                        ans.append(node)
                    else:
                        ans.append(node.val)
                        if node.left: queue.append(node.left)
                        else: queue.append(10001)

                        if node.right: queue.append(node.right)
                        else: queue.append(10001)
        
        bfs()
        p = ans
        ans = []
        queue = [q]
        bfs()
        q = ans
        print(p,q)
        if p == q : return True
        else: return False
        
