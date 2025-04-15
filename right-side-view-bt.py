# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def rDfs(root, depth):
            nonlocal res
            if not root:
                return None
            
            if len(res) == depth:
                res.append(root.val)

            rDfs(root.right, depth + 1)
            rDfs(root.left, depth + 1)

        rDfs(root, len(res))
        return res
        