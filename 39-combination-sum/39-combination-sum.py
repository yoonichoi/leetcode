class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, n = [], len(candidates)
        candidates.sort()
        
        def find(idx, target, path):
            if target < 0:
                return True
            if target == 0:
                res.append(path)
                return False
            for i in range(idx, n):
                if find(i, target-candidates[i], path+[candidates[i]]):
                    break
        find(0, target, [])
        return res