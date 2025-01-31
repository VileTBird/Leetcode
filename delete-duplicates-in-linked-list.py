'''
basically the problem is that we have to remove duplicates in a sorted linked list. 

for example 1->1->2->4

sorted is the key word, if there are duplicates in a sorted list, then the duplicates would be right next to each other.

so when we iterate thru the list with the curr pointer if we find the following node.val being equal to our curr.val
we basically change our curr.next or our current pointer to beyond the next node. if its not equal then its clearly not a duplicate
in that case we just shift our curr pointer to next node.

my original implementation was a bit different, where i basically implemented a nested while loop, where an extra nxt variable
which would initialized to each iterations curr pointer.
so if the linked list and on the first iteration of the loop

ex: 1(curr)->1(nxt)->1->2

with that we basically check with a while loop where as long as curr.val and nxt.val are equal, we increment the nxt pointer by one
or in othe words, we'll move nxt to the next node until the condiition is broken

in this case until it reaches 2
1(curr)->1->1->2(nxt)
and after it reaches 2
we basically change the pointer of curr pointer or curr.next to 2, skipping all the duplicates 
and in the end of the iteration and we shift the curr pointer itself to 2, this way our loop will skip all the duplicates
removing it from the list.

the performance differences are well not that big it would be a o(n) where each node will only be visited one. so im not dumb 
i just believe the more popular solution is a bit more simple with just two conditional statements, which is easier to read and 
technically its more efficient lol cus we use extra memory for the nxt var LOL
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head