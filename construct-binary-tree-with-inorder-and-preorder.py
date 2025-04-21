# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array = []

        def dfs(node):
            if node is None:
                return 0

            dfs(node.left)
            array.append(node)
            dfs(node.right)

        dfs(root)
        return array[k - 1].val
                    

                
        