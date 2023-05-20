"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        answer = []
        def recur(tree: Node):
            if tree is None:
                return
            for child in tree.children:
                recur(child)
            answer.append(tree.val)
        recur(root)
        return answer