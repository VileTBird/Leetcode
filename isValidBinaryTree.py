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
