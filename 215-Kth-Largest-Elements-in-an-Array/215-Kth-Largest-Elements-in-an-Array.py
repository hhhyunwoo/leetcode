from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inOrder(self, node):
        if node is None:
            return 
        self.inOrder(node.left)
        self.sortedArr.append(node.val)
        self.inOrder(node.right)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.sortedArr = []
        # Making Binary Search Tree
        tree = TreeNode(nums[0])
        for num in nums[1:]:
            root = tree
            nextNode = TreeNode(num)
            while root:
                if nextNode.val > root.val:
                    if root.right is None:
                        root.right = nextNode
                        break
                    else:
                        root = root.right
                else:
                    if root.left is None:
                        root.left = nextNode
                        break
                    else:
                        root = root.left
        self.inOrder(tree)

        return self.sortedArr[-k]

sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], 2))


################################
# Heap Solution

from queue import PriorityQueue

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = PriorityQueue()
        for num in nums:
            q.put(-num)
        
        for _ in range(k-1):
            q.get()
        return -1 * q.get()
        

sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], 2))