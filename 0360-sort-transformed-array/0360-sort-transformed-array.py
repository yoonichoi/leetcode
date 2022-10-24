class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        # def transform(a,b,c,x):
        #     return a*x**2 + b*x + c
        return sorted(list(map(lambda x: a*x**2 + b*x + c, nums)))