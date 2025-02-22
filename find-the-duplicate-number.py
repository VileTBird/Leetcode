'''
A bit rusty but this was a really fun problem to solve (yes im back)

for starters the easiest method to solve this problem would be to throw it all in a hashset or hashmap, seeing which element
appears more than once and immediately returning that said element. 

literally takes less than 4 lines of code but ofc it has to be hard. 

the second solution ima be honest i couldnt come up with it but i have a pretty good understanding of why it works without mathematical proof
(i derived why it works[proud])

anyways the problem solution requires two key checkpoints 

1. figuring out that its a linked list cycle problem
2. using floyds algorithm 

after u figure that out the rest is piss easy, assuming u understand the intuition ofc.

the core logic is u start with a fast and slow pointer, u move fast 2x speed. 

when they intersect u break

and u start a second pointer from start, init the old slow parallel in parallel by 1 until they meet.

why would this work exactly? 

to understand that u have to break away from the problem. 
if u look at a linked cycle starting from node x, initialize both slow and fast pointers from there, they will eventually meet at
node x. why? because fast basically just moves in 2x speed, with enough iteration they will meet at the beginning.

now what happens if u add a node or two at the beginning

for example a->b->x(cycle)

itll create an offset of 2 in our cycle, in other words, instead of fast and slow meeting at node x, they will meet two nodes before
x in the cycle. so when u start a second slow pointer from a, they only have two nodes to traverse to meet. 

hope that helped.
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1

            if hashmap[num] > 1:
                return num
        

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                break

        return slow
        
            