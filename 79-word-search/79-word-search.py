class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word: return True
        if not board: return False
        m, n, w = len(board), len(board[0]), len(word)-1
        
        def dfs(i,j,k):
            if i<0 or i>=m or j<0 or j>=n:
                return False
            if board[i][j] == '#':
                return False
            if board[i][j] != word[k]:
                return False
            
            # if last character and matched until so far:
            if k==w: 
                return True
            
            # if still in search
            k += 1
            tmp = board[i][j]
            board[i][j] = '#'
            
            # check all adjacent
            for x,y in ((-1,0), (1,0),(0,1),(0,-1)):
                if dfs(i+x, j+y, k):
                    return True
            
            board[i][j] = tmp
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False