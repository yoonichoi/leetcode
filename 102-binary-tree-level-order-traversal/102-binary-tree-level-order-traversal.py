# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            tmp = []
            for node in level:
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            level= tmp
            # level = [child for node in level for child in (node.left, node.right) if child]
        return ans