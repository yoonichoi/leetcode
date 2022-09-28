class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # start, end, cnt, e = [], [], 0, 0
        # for i in sorted(intervals):
        #     start.append(i[0])
        #     end.append(i[1])
        # print(start, end, cnt, e)
        # for s in range(len(start)):
        #     if start[s] < end[e]:
        #         cnt += 1
        #     else:
        #         e += 1
        # return cnt
        e = ret = 0
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals)
        
        for s in range(len(start)):
            if start[s] < end[e]: 
                ret += 1
            else: 
                e += 1
        return ret