class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        low, up = int(n*0.05), int(n*0.95)
        return sum(arr[low:up])/(up-low)
        