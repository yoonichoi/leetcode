class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[0]*(i+1) for i in range(numRows)]
        for r in range(len(ans)):
            ans[r][0] = ans[r][-1] = 1
            if len(ans[r]) > 2:
                for i in range(1, len(ans[r])-1):
                    ans[r][i] = ans[r-1][i-1] + ans[r-1][i]
        return ans