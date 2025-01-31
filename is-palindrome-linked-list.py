'''
i'VE solved so many medium problems but ive never struggled with a problem before lol. this is cancer. 

mostly due to how i jumped into linkedlist without implementation or practicing the data structure, we'll choose to ignore it lol

anyways anyways the first solution is pretty simple we just loop through the linked list, store it in an array, once we have that
we basically use two pointers to compare the entire list from right to left simultaneously

this would uh have a worst case time complexity of o(n + n) or o(2n) or o(n) which is pretty damn good imo, and space complexity is
o(n) this solution took me barely 2 mins to implement but ofc they have to make things harder

the constraints are we have to accomplish this in o(n) and o(1) memory

originally i tried accomplish this by essentially reversing the entire list in an attempt to create a new list and 
compare both but the problem was i was essentially corrupting and changing the data structure.

after with how i implemented reversal we essentially lost hte original linked list which is annoying. sure there are workarounds
but that would involve o(n) memory

theres a much more clever solution 

for starters we basically start with floyds hare and tortoise or whatever algorithm

where we increment fast pointer by 2 and slow pointer by 1. essentially we use this method to find the median of the linked list
or the middle or the closest to the middle, kinda like doing /2 if u invert ur perspective

anyways once we have that we basically reverse the linked list from the slow pointer.

for example if our list is 1->2->3->2->1 we basically reverse it to 1->2->3<-2<-1

we already know the reversing algorithm, where we start by shifting curr.next to null, then we shift prev to curr, following that
we shift curr to iriginal curr.next, by doing this our data structure would look something like this

1->2->3->null<-2<-1(prev) - null(curr)

and after reversal we know that curr is null but the prev is one behind that so we essentially have the last node or the right
most node. from here its pretty simple
we iterate once more thru the loop this time we compare from the left to right like two pointers.

left = head, right = prev. essentially the main loop condition is right shouldnt be null.

if in any case left and the corresponding right pointer do not match or not equal then we isntantly return false, cus we know its not a palindrome
on the other hand if its equal then itll end by the time right reaches null and the left will reach 3, we dont care about middle values

after the loop ends we instantly return True cus we know its a palindrome

a bit of a mental gymnastics i dont know how they expect u to derive this in an interview in 10 mins LOL but its kinda cool
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        nums = []

        curr = head

        while curr:
            nums.append(curr.val)
            curr = curr.next 

        l, r = 0, len(nums) - 1

        while l<=r:
            if nums[l] != nums[r]:
                return False
            
            l += 1
            r -= 1
        
        return True
    

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev, curr = None, slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        left = head

        right = prev

        while left and right:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next

        return True