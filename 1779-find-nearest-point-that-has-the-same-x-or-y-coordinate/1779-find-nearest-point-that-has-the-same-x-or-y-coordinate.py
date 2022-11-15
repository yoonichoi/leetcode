class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def manhattan(x1,y1,x2,y2):
            return abs(x1-x2) + abs(y1-y2)
        res = []
        for i, pts in enumerate(points):
            x1,y1 = pts
            if x == x1 or y == y1:
                res.append((i, manhattan(x,y,x1,y1)))
        return min(res, key=lambda x:x[1])[0] if res else -1