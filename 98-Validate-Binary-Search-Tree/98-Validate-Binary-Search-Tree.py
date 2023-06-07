# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from math import inf

class Solution:
    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        self.sortedList.append(node.val)
        self.inOrder(node.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.sortedList = []
        self.inOrder(root)
        maxNum = -1 * inf
        for num in self.sortedList:
            if num > maxNum:
                maxNum = num
            else:
                return False
            
        return True