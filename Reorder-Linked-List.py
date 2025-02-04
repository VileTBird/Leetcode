'''
Oh boy this was my first problem that I solved first try and its medium too. its absolutely euphoric! all the linked list muscle
isnt for nothing. spam the same pattern and u get really really good at it goddamn 

okay for starters the problem requires us to reorder the list, in other words they want us to insert from r to half, in between
each element in l to half.

so if its 2 4 6

they want 2 6 4 

pretty interesting problem, for starters we need to find the half, which we can just do by using fast and slow pointers

slow would end up at the half. next as soon as we end up there, we basically reverse from the second half, 

so we basically initialise our pointer from the next node after our middle point, and then we cut the second half from our middle point

then we just reverse the list pretty simple.

after we do that, we basically traverse the two lists until one of them becomes null, and while we traverse them we point
the node at left pointer to the node at right pointer, and then we point the node at right pointer to the node that originally came
aftter left pointer, essentially mergign it. ofc we store temp variables but thatsd fine i think u get htat. 

finally we dont have to return anything we only have to modify the list. 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev, curr = None, slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        l, r = head, prev 

        while r and l:
            lnxt = l.next
            rnxt = r.next
            l.next = r
            r.next = lnxt
            l = lnxt
            r = rnxt    