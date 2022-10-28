class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = len(matrix)
        c = len(matrix[0])
        ans = []
        top, bottom, left, right = 0, r-1, 0, c-1
        while top <= bottom and left <= right:
            for col in range(left, right+1):
                ans.append(matrix[top][col])
            top += 1
            for row in range(top, bottom+1):
                ans.append(matrix[row][right])
            right -= 1
            for col in range(right, left-1, -1):
                ans.append(matrix[bottom][col])
            bottom -= 1
            for row in range(bottom, top-1, -1):
                ans.append(matrix[row][left])
            left += 1
        return ans[:r*c]