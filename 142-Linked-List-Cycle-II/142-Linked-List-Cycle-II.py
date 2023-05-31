# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        tortoise, hare = head, head
        flag = False

        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                flag = True
                break
        if flag is False:
            return None
            
        tortoise = head
        while True:
            if tortoise == hare:
                return tortoise
            tortoise = tortoise.next
            hare = hare.next
        return None