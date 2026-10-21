
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        while prev and temp:
            nxt = temp.next
            temp.next = prev
            temp = nxt

            nxt = prev.next
            prev.next = temp
            prev = nxt

            

        



         
         
        
        

        
        
        