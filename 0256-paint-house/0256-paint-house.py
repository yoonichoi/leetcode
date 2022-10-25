class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        r, b, g = 0, 0, 0
        for cr, cb, cg in costs:
            r, b, g = min(b,g) + cr, min(r,g) + cb, min(r,b) + cg
        return min(r,b,g)