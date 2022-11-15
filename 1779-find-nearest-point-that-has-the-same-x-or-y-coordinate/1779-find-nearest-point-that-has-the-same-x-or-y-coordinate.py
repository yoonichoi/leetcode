class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minn, ans = float('inf'), -1
        for i, (a,b) in enumerate(points):
            if x==a or y==b:
                mandist = abs(x-a) + abs(y-b)
                if mandist < minn:
                    ans, minn = i, mandist
        return ans