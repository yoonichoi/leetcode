class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix)
        width = len(matrix[0])
        top, left = 0, 0
        bottom, right = height-1, width-1
        ans = []
        while top<bottom and left<right:
            for col in range(left, right):
                ans.append(matrix[top][col])
            for row in range(top, bottom):
                ans.append(matrix[row][right])
            for col in range(right, left, -1):
                ans.append(matrix[bottom][col])
            for row in range(bottom, top, -1):
                ans.append(matrix[row][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        if len(ans) < height * width:
            for row in range(top,bottom+1):
                for col in range(left, right+1):
                    ans.append(matrix[row][col])
        return ans