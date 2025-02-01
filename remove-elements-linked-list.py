'''
Dummy nodes are ingenious, humanitys greatest invention im telling you! lol.
the question itself is pretty straigt forward, u have to remove nodes that are equivalent to the given value,

sounds pretty easy, u loop thru the linked list and while u loop thru it, u basically see if the next node has a value equal to
that of our target, if it is, we skip that node and we assign the following node to our curr.next pointer. 

if its not equal we just move our curr pointer to the next node, pretty straight forward problem but theres an annoying edge case
what if the first element/node is equal to that of our target? in that case we cant return head cus head could get skipped potentially 

and when we loop thru the linked list, we only check .next.val not curr in that case the head will get completely skipped over

but despite this glaringly annoying edge case/bug my first solution was accepted by LEETCODE LOL.

anyways the second solution is pretty simple and actually straight forward the only difference is, we make a dummy node with -1
and point its .next to our head and we place our curr pointer on our dummy node. in this case our original head will be checked

and ofc in the end when we return it, we could just return dummy.next cus even if our head is problematic dummy would simply point
to some other following node that doesnt equal target or itll pass to null either way it works for us. ez peasy
'''

class Solution(object):
    def removeElements(self, head, val):
        '''CAUTION THIS SOLUTION IS BUGGY, ALTHOUGH ITS ACCEPTED BY LEETCODE IT HAS AN EDGE CASE OR A LOGIC ERROR, 
        PRIMARILY WITH CHECKING THE FIRST HEAD NODE

        so for example if curr.val is equal to our target value, itll be skipped or ignored and the logic with i is kinda flimsy
        even though it works.

        to fix the logic bug id prolly add a conditional at the start of the loop to check for curr.val if its equal we shift
        to next or a nested while loop would be better imo. but im not doing either of that cus the second solution is better.
        '''
        curr = head
        newHead = None
        i = 0
        while curr:
            if curr.next is not None and curr.next.val == val:
                curr.next = curr.next.next
            else:
                if i == 0 and curr.val != val:
                    newHead = curr
                    i += 1
                curr = curr.next
                

        return newHead
        

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        while curr:
            if curr.next is not None and curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                

        return dummy.next
        