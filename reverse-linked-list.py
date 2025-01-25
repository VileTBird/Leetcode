class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        l = head
        curr = head

        while l:
            l = l.next
            curr.next = prev
            prev = curr
            curr = l
        
        return prev
        