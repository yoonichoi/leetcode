# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def d(root, depth):
            if not root: return depth
            return max(d(root.left, depth+1), d(root.right,depth+1))
        return d(root, 0)