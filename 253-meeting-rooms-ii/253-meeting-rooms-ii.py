class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        cnt, e = 0, 0
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)
        print(start, end, cnt, e)
        for s in range(len(start)):
            if start[s] < end[e]:
                cnt += 1
            else:
                e += 1
        return cnt