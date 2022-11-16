# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        def dfs(root, target, heap):
            if not root: return
            dfs(root.left, target, heap)
            heapq.heappush(heap, (abs(root.val-target), root.val))
            dfs(root.right, target, heap)
        heap = []
        dfs(root, target, heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res