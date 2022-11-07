# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isMatch(p,q):
            if not p and not q: return True
            elif not p or not q: return False
            else:
                if p.val == q.val:
                    return isMatch(p.left, q.left) and isMatch(p.right, q.right)
        if isMatch(root, subRoot): return True
        if not root: return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        