class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        n = len(candidates)
        def dfs(cur, cur_sum, idx):
            if cur_sum > target:
                return
            if cur_sum == target:
                res.append(cur)
                return
            for i in range(idx, n):
                dfs(cur+[candidates[i]], cur_sum + candidates[i], i)
        dfs([], 0, 0)
        return res
        