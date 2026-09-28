# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        a = head
        no = 0

        while a:
            no += 1
            a = a.next

        b = no // k

        prev = None
        count = 0
        x = 0
        first = None
        last = None

        while x < b:

            count = 0
            prev = None
            start = temp

            while temp and count < k:
                nxt = temp.next
                temp.next = prev
                prev = temp
                temp = nxt
                count += 1

            if first is None:
                first = prev
            else:
                last.next = prev

            last = start
            x += 1

        last.next = temp

        return first
        
        
        
            


        