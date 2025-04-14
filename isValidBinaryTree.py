'''
I think this is areally good problem to solve got my mind working and shit. 

at the start they want us to validateif something isa  binary search tree, binary search trees are ordered in a very specific way for example 

the nodes on the left side are always smaller than the subtrees root nodeand every other "root" node in the tree and its the opposite in the right side. 

but theres a specification 

this also applies to both branches 

lets say it goe something lik 1 -> 2, 2-> 1.5, 2-> 4 if on the right side it was something like that it doesnt matter if 1.5 is on the lef tsdie of the subtree
it should be greater than 1

with that rule outta the way the mostbrute force way to do thissolution would be to visit every single node and compare it with our list of root nodes and what not
this would mean visiting n nodes for each tree and subtrees, it would be a n * n or o(n^2) solution 

this is why we instead do something a bit more efficient instead we update our lower bound and upper bound, so that we check if each node fits the rule
forour lower boundand upper bound, which would only require us to visit each node once (we can iteratively update lower and upper bound as needed) and finally
it would only require us to hold two values in memory.

how would we do this? intiially we dfine our lower abd upper bound as some arbitrary variables called _min and _max, we can uhm store -inf and positive infinity
for our initial min max, then in our recursive function we do two things first our base condition if our node hits None it meant it never got a false, 
in other words it reached the end of the tree satisfying all conditions so we return True

and our second conditional for when we return false, we basically check if our current node value is smaller than our minimum or lower bound or bigger than our upper bound or maximum
if it is we return false 

thats basically it, then we recursively call the function this is where it gets tricky, lets visualize this from our root root node

from our root node our recusive function should be called on both sides of our tree, for one on the left side all values are smaller than our node.val
that is the goal, so in each function call we basically set out upper bound for the left side of the tree as the subtrees root node, in other words if a subtrees
root node passes the conditions for lower and upper bound itll basically be the new upperbound for the left side of tree. ofc itll recusrively call it for both its lef tand right

next ont he right side all values should be greater than our root node, in other words we update our minimum or lower bound to be equal to our subtrees root node
or current node that has passed our conditions for a valid node. 

once we do that its relatively simple we basically and the results from both left and right so that we can know for sure if both sides return true

and finally we return the boolean result!
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def valid(node, _min, _max):
            if node is None:
                return True
            if not (node.val > _min and node.val < _max):
                return False
            
            return(valid(node.left, _min, node.val) and valid(node.right, node.val, _max))

        return valid(root, float("-inf"), float("inf"))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node, _min, _max):
            if node is None:
                return True
            
            if not (node.val > _min and node.val < _max):
                return False

            return (isValid(node.left, _min, node.val) and isValid(node.right, node.val, _max))

        return isValid(root, float("-inf"), float("inf"))