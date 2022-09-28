class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals or len(intervals) == 1: return True
        intervals.sort()
        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True
    
    