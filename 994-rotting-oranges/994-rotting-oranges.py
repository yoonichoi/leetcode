class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n, fresh, time = len(grid), len(grid[0]), 0, 0
        rotten = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i,j))
        while rotten and fresh > 0:
            time += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                    nx,ny = x+dx, y+dy
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] != 1:
                        continue
                    grid[nx][ny] = 2
                    fresh -= 1
                    rotten.append((nx,ny))
        return -1 if fresh > 0 else time