# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array = []

        
        def buildArray(root):
            nonlocal array
            if root is None:
                return None

            array.append(root.val)

            buildArray(root.left)
            buildArray(root.right)

        buildArray(root)

        array.sort()

        k = k - 1

        return array[k]
        