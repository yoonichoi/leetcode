# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isMatch(a,b):
            if not a and not b: return True
            elif not a or not b: return False
            else:
                if a.val == b.val:
                    return isMatch(a.left, b.left) and isMatch(a.right, b.right)
        if isMatch(root, subRoot): return True
        if not root: return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
