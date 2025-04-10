# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Definition for a binary tree node.

        if not root:
            return []
        q = deque()
        q.append((root, 0))
        res = []
        while q:
            node, depth = q.popleft()

            if depth == len(res):
                res.append([])

            if node:
                res[depth].append(node.val)
                if node.left:
                    q.append((node.left, depth+1))
                if node.right:
                    q.append((node.right, depth+1))
        

        return res
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        q = deque()
        q.append((root, 0))
        res = []
        while q:
            node, depth = q.popleft()

            if depth == len(res):
                res.append([])

            if node:
                res[depth].append(node.val)
                if node.left:
                    q.append((node.left, depth+1))
                if node.right:
                    q.append((node.right, depth+1))
        
        if res == [[]]: res = []
        return res
        