class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        currend, cnt = float('-inf'), 0
        for s,e in sorted(intervals, key=lambda x:x[1]):
            if s < currend:
                cnt += 1
            else:
                currend = e
        return cnt
                