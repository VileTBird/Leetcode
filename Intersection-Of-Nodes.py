# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nums = set()

        curr = headA

        while curr:
            nums.add(curr)
            curr = curr.next

        while headB:
            if headB is not None and headB in nums:
                return headB
            headB = headB.next
        
        return None
    

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1, l2 = headA, headB

        length1, length2 = 0, 0 

        while l1:
            l1 = l1.next
            length1 += 1

        while l2:
            l2 = l2.next
            length2 += 1

        r1, r2 = headA, headB

        if length2>length1:
            i = length2 - length1
            while i != 0:
                r2 = r2.next
                i -= 1
        elif length1>length2:
            i = length1 - length2
            while i != 0:
                r1 = r1.next
                i -= 1

        while r2 and r1:
            if r1 == r2:
                return r1
            
            r1 = r1.next
            r2 = r2.next

        return None