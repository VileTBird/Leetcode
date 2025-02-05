'''
Okay so this is a kind of a tricky problem but i was able to solve it but there is afollow up and i didnt even know abt it
stupid neetcode. i should prolly stick to leetcode anyways anyways 

for starters the most brute force way would be to put this in an array remove it from the back or loop from the back and remove that elemnt
and then make it a linked list agin

the second more optimal o(n) solution with o(1) space would be to first reverse the list, traverse it from reverse, decrement until
we reach our chosen point, when we reach that point we just skip it and continue reversing the list bacck.
this would be two pass. still efficient

there is a much more optimal solution this is also o(n).

here we use two pointers, essentially we loop n times first to get our faster pointer ahead, then we loop again but only this time
we also loop our slow pointer in parallel until our faster pointer reaches null 

so why would this work exactly, its not a very intuitive solution, the core knowledge is u need the length to figure out which node to delete

and this raises a core question what if you could keep track of length without explicitly having the length?

thats what our second solution does,

essentially at the start we move our fast pointer by n, creating an offset. once this si done we increment both pointers at the 
same time until fast reaches null 

why would this work exactly? you have to understand when we incrememnt both at the same time, fast pointer is ahead of slow by
n elements. in other words when fast reaches null, slow is behind of null by n elements, at the exact point we have to delete.

if we offset slow by -1 then we reach the point thats before the node we have to delete which can be easily done by skipping the 
next node with .next.next
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            cnxt = curr.next
            curr.next = prev
            prev = curr
            curr = cnxt

        curr, prev = prev, None
        
        p = prev 
        k = n
        while curr:
            k -= 1
            if k == 0:
                curr = curr.next
            else:
                cnxt = curr.next
                curr.next = prev 
                prev = curr
                curr = cnxt 
                
        
        
            
        return prev 
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        slow, fast = dummy, head

        while n > 0 and fast:
            fast = fast.next
            n -= 1
        
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        
        return dummy.next

        