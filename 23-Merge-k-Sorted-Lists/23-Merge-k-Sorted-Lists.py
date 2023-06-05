# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        numArr = []
        for linkedList in lists:
            while linkedList:
                numArr.append(linkedList.val)
                linkedList = linkedList.next
        sortedNumArr = sorted(numArr)

        answer = ListNode()
        nextNode = answer

        for num in sortedNumArr:
            nextNode.next = ListNode(num)
            nextNode = nextNode.next

        return answer.next