class TimeMap(object):

    def __init__(self):
        self.dic = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.dic[key].append((value, timestamp))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key in self.dic:
            li = self.dic[key]
            l, r = 0, len(li)-1
            if li[l][1] > timestamp:
                return ""
            elif li[r][1] <= timestamp:
                return li[r][0]
            else:
                while l<= r:
                    mid = l+(r-l) // 2
                    if li[mid][1] == timestamp:
                        return li[mid][0]
                    if li[mid][1] < timestamp:
                        l = mid +1
                    else:
                        r = mid -1
                return li[r][0]           
        return ""
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)