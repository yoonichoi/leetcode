class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(x,y,grid):
            if x < 0 or x>=m or y<0 or y>=n or grid[x][y] != '1':
                return
            grid[x][y] = '#'
            for dx, dy in ((0,1),(0,-1),(-1,0),(1,0)):
                nx, ny = x+dx, y+dy
                dfs(nx, ny, grid)
        m, n, cnt= len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j,grid)
                    cnt += 1
        return cnt