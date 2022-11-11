class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        ans = [''] * numRows
        row_idx = 1
        going_up = True
        for c in s:
            ans[row_idx-1] += c
            if row_idx == numRows:
                going_up = False
            if row_idx == 1:
                going_up = True
            if going_up:
                row_idx += 1
            else:
                row_idx -= 1
        return ''.join(ans)
        
        
        
        