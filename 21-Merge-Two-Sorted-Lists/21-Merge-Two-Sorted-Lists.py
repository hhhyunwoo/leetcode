# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1List, list2List = [], []
        print(list1)

        while list1:
            list1List.append(list1.val)
            list1 = list1.next

        while list2:
            list2List.append(list2.val)
            list2 = list2.next
        sortedList = sorted(list1List+list2List)

        answer = ListNode()
        print(answer)
        nextList = answer
        for val in sortedList:
            nextList.next = ListNode(val)
            nextList = nextList.next
        print(answer)
        
        return answer.next