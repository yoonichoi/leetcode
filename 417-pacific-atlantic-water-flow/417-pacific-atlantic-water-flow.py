class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]: return []
        m, n = len(heights), len(heights[0])
        def bfs(start):
            q = collections.deque(start)
            visited = set(start)
            while q:
                x, y  = q.popleft()
                for dx,dy in ((x,y+1),(x,y-1),(x-1,y),(x+1,y)):
                    if 0<=dx<m and 0<=dy<n and (dx,dy) not in visited \
                    and heights[dx][dy] >= heights[x][y]:
                        q.append((dx,dy))
                        visited.add((dx,dy))
            return visited
        
        pacific = [(0,c) for c in range(n)] + [(r,0) for r in range(1,m)]
        atlantic = [(r,n-1) for r in range(m)] + [(m-1, c) for c in range(n-1)]
        
        return bfs(pacific) & bfs(atlantic)