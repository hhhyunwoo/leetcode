# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeList = []
        while head:
            newNode = ListNode(head.val)
            nodeList.append(newNode)
            head = head.next
        answer = ListNode()
        nextNode = answer
        
        for i in reversed(range(len(nodeList))):
            nextNode.next = nodeList[i]
            nextNode = nextNode.next
        return answer.next