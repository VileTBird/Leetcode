'''
this is a very fun problem to solve. once u know the solution of course. lol.

anyways this is pretty striaght forward, u just have to make a copy of a linked list with the same values and pointers but with new nodes
this would be straight forward to do but each node has also a random pointer that points to a random node in the list.

this would cause a problem if our new node hasnt been created yet and even .nex would be a problem cus we cant reference a node
that hasnt been creatd a yet 

a hashmap would easily solve this yes a hashmap. have i ever talked abt how hashmaps are humanitys greatest creation?

anyways we first create copy nodes with the same values and map it to our original nodes in the hashmap, and next in the hashmap
we just map our curr.next and curr.random to its equivalent in the hashmap and get that values and assign those to our
copy.next and copy.random 

ofc theres a tiny edge case what if random or next points to None? we create a init with None: None to essentially return None
solving this tiny annoying edgy case.

essentially creating a deep copy at the end 
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None : None}

        curr = head
        while curr:
            copy = Node(curr.val)
            hashmap[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = hashmap[curr]
            copy.next = hashmap[curr.next]
            copy.random = hashmap[curr.random]
            curr = curr.next

        return hashmap[head]
        