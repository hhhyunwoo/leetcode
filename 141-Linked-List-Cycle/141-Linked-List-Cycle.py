class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        tortoise, hare = head, head
        while True:
            if head.next is None or head.next.next is None:
                return False
            tortoise = head.next
            hare = head.next.next

            if tortoise == hare:
                return True
