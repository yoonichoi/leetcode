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
        if not root: return []
        q, res = collections.deque([root]), []
        while q:
            level, size = [], len(q)
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
            res.append(level)
        return res
    
        # ans, level = [], [root]
        # while root and level:
        #     ans.append([node.val for node in level])
        #     tmp = []
        #     for node in level:
        #         if node.left: tmp.append(node.left)
        #         if node.right: tmp.append(node.right)
        #     level= tmp
        # return ans
    
    