# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        def findGoodNodes(node, _max):
            if node is None:
                return 0

            res = 0

            if node.val >= _max:
                res += 1
                return res + findGoodNodes(node.left, node.val) + findGoodNodes(node.right, node.val)
            else:
                return res + findGoodNodes(node.left, _max) + findGoodNodes(node.right, _max)   


        return findGoodNodes(root, float("-inf"))
