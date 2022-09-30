class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        q = collections.deque([])
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r,c))
                else:
                    mat[r][c] = -1
        while q:
            r, c = q.popleft()
            for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
                nr, nc = r+dx, c+dy
                if nr < 0 or nr==m or nc<0 or nc==n or mat[nr][nc] != -1:
                    continue
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr,nc))
                
        return mat
        