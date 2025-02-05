'''
this was a very fun problem to solve cus i was actually able to solve it LOL. 

anyways anyways key points are we have two linked lists, that have each digit of a number, if u concatenate it should add up to a number

3 -> 2 -> 1

321 

but the problem is its in reverse order 

so its not acc 321 but 123 

with that outta the way the problem requires us to find the addision of two of these linked lists. 

my solution is o(n + m + k) mind you! and o(1) but its not the most optimal solutoion and it can be considered suboptimal because we make
3 loops in total essentially separately, k would be the resulting number from adding n and m 

anyways with tha tout the way the core logic is we get the numbers from each list by traversing and concateing each digit to a string
and finally we convert each str to int and add and finally we traverse our result string from reverse and add each digit to our 
new linked list. 

ezpz 

anyways

the more optimal solution would be to taking advantage of the two lists being in reverse order 

like actual addition we add in reverse 

we traverse both lists in parallel and add their values, ofc what if the list pointers already reach null? 

we just have an if condition to keep them as None and not travcerse anymore and have an if condition to have the corresponding value
as 0. 

finally the carry condition, for carrys we basically add the single digit and divide it by 10. so for 22 it would be 2.2

and we round this so itll be 2. what if theres no carry? for example 5 would be 0.5 if we round this itll be just 0.

we just add carry as a condition to our while loop in case our carry is not empty from our very last addition. for example
if the final elements are 6 and 5, we'll create a node for 1 but we need to carry 1 and make a node for that.

if u remember from before if our pointers for our l1 and l2 are None we just store them as None and get the corresponding value as 0

so we just need to add those two values with carry like usual. resulting in a carry node without us doing anything! 

very very nice. man i love leetcode.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = l1
        no1 = ""

        while curr:
            no1 = str(curr.val) + no1
            curr = curr.next
        
        curr = l2
        no2 = ""
        while curr:
            no2 = str(curr.val) + no2
            curr = curr.next

        dummy = ListNode(0)
        curr = dummy
        no3 = str(int(no1) + int(no2))
        for i in range(len(no3)-1, -1, -1):
            curr.next = ListNode(no3[i])
            curr = curr.next
        
        return dummy.next
            


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0 

            val = v1 + v2 + carry

            carry = val // 10
            v = val % 10

            curr.next = ListNode(v)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
            


