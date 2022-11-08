class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = set()
        res = False
        
        def dfs(i,j,visited,word,index):
            if index == len(word): return True
            if i<0 or j<0 or i>=m or j>=n or (i,j) in visited or word[index]!=board[i][j]:
                return False
            visited.add((i,j))
            res = (dfs(i+1,j,visited,word,index+1) or
                dfs(i-1,j,visited,word,index+1) or
                dfs(i,j+1,visited,word,index+1) or
                dfs(i,j-1,visited,word,index+1))
            visited.remove((i,j))
            return res
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i,j,visited,word,0):
                        return True
        return False