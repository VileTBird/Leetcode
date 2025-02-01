'''
Okay so this was a pretty fun problem to play with, honestly the only annoying part is the constraints, if it wasnt for that itd
actually be an *easy* problem LOL

for starters the question wnats us to find the intersection point. how would u do that?

the easy way would be to traverse the first linked list, store all its elements in a hashset, and we loop thru the second linked list
and see if each element is in the hashset 

the first element to be in the hashset is what we return. honestly its not a ingenious solution but simplicity>

ofc leetcode has to make ti complicated cus this solution is o(n+m) for time complexity and o(n) for space

so we have to think smarter, 

one way would be to find the lengths of respective list and start from the same respective position, this is the easy and most
straight forward way, for example if we have a linked list of length 6 intersecting with a linked list of length 5,
we basically loop thru the entire linked list to find the respective lengths, after we do that we could just subtract them and
shift the linked list with length 6 by 1, so linked list one would start from [1] position instead of [0]
in that case it would be easy we just see if theyre equal anywhere if they are we return that node, if not we return the None at the end

although this solution works, it is optimal with o(n+m) time complexity and o(1) space complexity

but its still suboptimal, we do a total of 2 loops + 2 conditionals + 2 nested loops to shift the starting point of our longer list

the easier way is a lot more elegant but not very intruitive, for starters we start a loop where itll loop as long as each node
in the list arent equal. so we loop thru until the very end where atleast one list reaches null or None, if that happens we shift
the pointer of that list to the head of the second list and vice versa for pointer 2.

why would this work exactly? think of it like this. if we have two intersecting lists head A and headB of sizes 5 and 3, 
how long would it take for one the pointer in the longer list to reach head of the second list? exactly 5 + 1 jump in that meantime
the second list with the size of 3 would also do a 5 + 1 jump so where would that be? after the second position of the first list
or in other words exactly where the two lists start to attain an equal length

1->2->3->4->5

      6->4->5

these are the two intersecting lists if we have two pointers l1 and l2

1->2->3(l2)->4->5

6(l1)-> 4 -> 5

by the time l1 reaches 6 l2 would exactly be at 3, from node 3 and 6 the list is of the same length, so when both pointers reach
the while loop would break cus l1 == l2 now.

okay this is cool but what if theres no intersection? this would work very elegantly 

cus if they are not intersection lets say these two new lists are like this,

1->2->3(l2)->4->5

6(l1)-> 7 -> 8

then still l1 and l2 would exactly be in the equivalent starting position, so even if we compare both pointers would reach None
or null at the exact same time 

1->2->3->4->5->null(l2)

6-> 7 -> 8 ->null(l1)
so the loop would break and return null

easy peasy

'''

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

        while l1 != l2:
            if l1: l1 = l1.next 
            else: l1 = headB

            if l2: l2 = l2.next
            else: l2 = headA

            
        return l1