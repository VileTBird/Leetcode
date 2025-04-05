# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if root is None:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            isbalanced = abs(left[1] - right[1]) <= 1

            isbalanced = left[0] and right[0] and isbalanced

            return [isbalanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]