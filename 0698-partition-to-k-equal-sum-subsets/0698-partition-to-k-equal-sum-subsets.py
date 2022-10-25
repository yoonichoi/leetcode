class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        buck, ksum = [0]*k, sum(nums)//k
        def dfs(idx):
            if idx == len(nums): return len(set(buck)) == 1
            for i in range(k):
                buck[i] += nums[idx]
                if buck[i] <= ksum and dfs(idx+1): return True
                buck[i] -= nums[idx]
                if buck[i] == 0: break
            return False
        return dfs(0)