# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        h = head

        while h:
            h = h.next
            count += 1

        if n == count:
            return head.next

        a = count - (n + 1)

        curr = head

        for i in range(a):
            curr = curr.next

        curr.next = curr.next.next

        return head



