"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return node
        q, clone = collections.deque([node]), {node.val: Node(node.val, [])}
        while q:
            curr = q.popleft()
            curr_clone = clone[curr.val]
            for ngbr in curr.neighbors:
                if ngbr.val not in clone:
                    clone[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)
                curr_clone.neighbors.append(clone[ngbr.val])
        return clone[node.val]
        