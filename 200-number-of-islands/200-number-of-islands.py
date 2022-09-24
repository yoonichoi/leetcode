class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        def dfs(grid,i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] != '1':
                return
            grid[i][j] = '#'
            for x, y in ((-1,0),(1,0),(0,-1),(0,1)):
                dfs(grid, i+x, j+y)
                
        m, n, cnt = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    cnt += 1
        return cnt