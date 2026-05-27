class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        1. Instead of finding surrounded regions, find unsurrounded regions and run
        dfs. Change any Os connected to edge to T.
        2. Now of the remaining board that is still 0s, change them to 'X'.
        3. Now change the T's back to 'O'
        """
        ROW,COL = len(board),len(board[0])

        def dfs(r,c):
            if (r < 0 or c < 0 or r == ROW or c == COL or board[r][c] != 'O'):
                return
            board[r][c] = "T"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(ROW):
            if board[r][0] == 'O':
                dfs(r,0)
            if board[r][COL-1] == 'O':
                dfs(r,COL-1)

        for c in range(COL):
            if board[0][c] == 'O':
                dfs(0,c)
            if board[ROW-1][c] == 'O':
                dfs(ROW-1,c)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"        
        