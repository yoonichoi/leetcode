class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = collections.defaultdict(list)
        larger = 0
        for num, cnt in collections.Counter(nums).items():
            dic[cnt].append(num)
            larger = max(larger, cnt)
        res = []
        for freq in range(larger, 0, -1):
            res.extend(dic[freq])
            if len(res) >= k:
                return res[:k]
        return res[:k]