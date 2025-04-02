'''
This was a pretty simple problem hope other problems CAN be this simple lol. the question basically wants us to invert tree so basically when there are two nodes left, right it should become right, left

im sure even Null nodes count here, it sounds straightforward, we just have to traverse down the tree depth or breath first approach, ahd for each ode we just have 
to do a switch for left to right 

to code it up its pretty simple we start with the base case where if root is none then we return none if not we assign the right leaf node to left, and the left leaf node to right
and then we recursively call our own function on our children left and right nodes so that the effect propagates! was fun to implement although i kinda 
knew the solution righ taway!

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root