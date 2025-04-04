'''
This was a pretty interesting problem to solve, quite tricky but I was still able to solve which is the fun part. Anyways the problem wants us to figure out
in the given two trees they want us to figure out if the second tree is a subtree of the first tree. 

First how would we do this? 

the easiest most brute force method would be to compare every single node and their respective subtrees but this can be optimized further by simply just
checking when each subtrees root node is equal to our given trees root node then we compare their respective subtrees. 

here we reuse our sametree function from the other problem, basically we just recursively compare first the elft side of one tree with the left side of the other
tree recursively if it evaluates to equal or true then we check the right side respectively. 

once we have this we'll have a bool as the return value, with that return value we could basically check if our Tree is the same, if the return value is true
we know that our given subtree is the subtree of our given root tree, we instantly return to true. if not then we just recursively call the issubtree 
first on the .left leaf node of our root node with our given subtree, and then we just "or" it and call it on .right leaf node of our root node with our subtrees root node

this will basicallyt check both left and right respectively and the or operator would make sure that if at any point in time either side figures out the res, then it'll
return as true.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool: 
        if root is None:
            return False

        if self.isSameTree(root, subRoot):
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

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