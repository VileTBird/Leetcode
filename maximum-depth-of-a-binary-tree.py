'''

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        stack = [[root, 1]]
        depth = 1

        while stack:
            node, temp = stack.pop()
            depth = max(depth, temp)
            if node.right:
                stack.append([node.right, temp+1])
            
            if node.left:
                stack.append([node.left, temp+1])
        
        return depth