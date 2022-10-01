class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        ls = []
        for p in points:
            x, y = p
            ls.append(([x,y], (x**2 + y**2)**0.5))
        return [i for i,v in sorted(ls, key=lambda x:x[1])[:k]]
    
    