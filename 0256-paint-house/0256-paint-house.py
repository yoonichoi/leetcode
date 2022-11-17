class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        r,b,g = 0,0,0
        for cr, cb, cg in costs:
            r,b,g = cr + min(b,g), cb+min(r,g), cg+min(r,b)
        return min(r,b,g)