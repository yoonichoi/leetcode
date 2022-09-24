class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]: return []
        m, n = len(heights), len(heights[0])
        p_visited = set()
        a_visited = set()
        
        def dfs(i, j, visited):
            if (i,j) in visited:
                return
            visited.add((i,j))
            for dx, dy in ((1,0),(-1,0),(0,-1),(0,1)):
                x, y = i+dx, j+dy
                if 0<=x<m and 0<=y<n:
                    if heights[x][y] >= heights[i][j]:
                        dfs(x,y,visited)
                
        for i in range(m):
            dfs(i, 0, p_visited)
            dfs(i, n-1, a_visited)
        for j in range(n):
            dfs(0, j, p_visited)
            dfs(m-1, j, a_visited)
        
        return list(p_visited & a_visited)