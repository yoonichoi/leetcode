class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals or len(intervals) == 1: return True
        intervals = sorted(intervals, key=lambda x:x[0])
        s,e = intervals[0]
        for i in intervals[1:]:
            if i[0] < e:
                return False
            s, e = i
        return True