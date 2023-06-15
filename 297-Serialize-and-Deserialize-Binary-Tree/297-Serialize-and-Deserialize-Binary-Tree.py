# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append('null')

        return ' '.join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return []
        data = data.split()

        for i in range(len(data)):
            data[i] = TreeNode(data[i])

        for i in range(1, len(data)+1):
            if i*2 <= len(data):
                data[i-1].left = data[i*2 - 1]
            if i*2+1 <= len(data):
                data[i-1].right = data[i*2+1 - 1]
        
        return data[0]

        


    
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))