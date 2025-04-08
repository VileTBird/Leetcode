'''
This is a very interesting problemn to solve i suppose unfortunatley i couldnt figure out initilaly myself mostly because of my personal biases 

and incorrect assumtioins 

anyways the problem itself is pretty easy 

first they want us to find the lowerst common ancestor of towo given nodes in other words the lowest node possible that is above them

so in two nodes it could either be the node thats dirtecftly causing a split or it could be one of those nodes causing said split

so in that case the traversal becomes realy really simple, if our curr pointer node is greater than both of our indiivdual nodes
then we go left cus we know it must be in the left side, if its leser then we know it must be on right side so we go right

when we finally find a node where its not greater nor lesser for one of our given nodes, or if each of the nodes hav to go in spearate ways
we know theres the lca, the node thats causing the split! we just return that node cus thats our result!
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            if cur.val > p.val and cur.val > q.val:
                cur = cur.left
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right
            else:
                return cur