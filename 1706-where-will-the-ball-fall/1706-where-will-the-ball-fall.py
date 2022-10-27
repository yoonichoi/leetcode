class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        r, c = len(grid), len(grid[0])
        def drop(i,j):
            if i == r:
                return j
            if j == c-1 and grid[i][j]== 1: return -1
            if j == 0 and grid[i][j] == -1: return -1
            if grid[i][j] == 1 and grid[i][j+1] == -1: return -1
            if grid[i][j] == -1 and grid[i][j-1] == 1: return -1
            return drop(i+1, j+grid[i][j])
        return [drop(0,j) for j in range(c)]