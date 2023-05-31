# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        tortoise, hare = head, head
        while True:
            if hare is None or hare.next is None:
                return False
            tortoise = tortoise.next
            hare = hare.next.next

            if tortoise == hare:
                return True
