class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        square = collections.defaultdict(list)
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows[r] or \
                    board[r][c] in cols[c] or \
                    board[r][c] in square[(r//3, c//3)]:
                    return False
                rows[r].append(board[r][c])
                cols[c].append(board[r][c])
                square[(r//3,(c//3))].append(board[r][c])
        return True