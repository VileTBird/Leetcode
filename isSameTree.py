'''
This was a very simple problem to sdolve, didnt take long. they basically want us to find if two give trees with root p and q are identical. 

so identical implies that they are structurally identical and each corresponding node is equal 

for one the basic recursion would be basically comparing if two nodes are equal, dfs only does one subtree at ta time, so we first check left and if its true
then we check right. 

btu what about the edge/base cases. what if theres two null nodes, or one null node and one non-null node, we have no option but to manually cancel out those 
edge cases with a buncha conditionals. 

i do understanbd that the code could be condensed further with and or operators but eh ima leave it like this so that i can understand my thought process if i refer back. 

ill attach the condensed soluition as well. 

the worst case time compledxity would be o(p + q) in case we have to traverse to ever single node
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None and q is not None:
            return False
        elif p is not None and q is None:
            return False
            
        res = True
        if p.val == q.val:
            res = self.isSameTree(p.left, q.left)
            if res:
                res = self.isSameTree(p.right, q.right)
        else:
            res = False
        
        return res


        