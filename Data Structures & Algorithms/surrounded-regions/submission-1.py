class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS = len(board),len(board[0])
        def dfs(x,y):
            if x < 0 or y < 0 or x >= ROWS or y >= COLS or board[x][y] != 'O':
                return
            board[x][y] = 'T'
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
        
        for r in range(ROWS):
            if board[r][0] == 'O':
                dfs(r,0)
            if board[r][COLS-1]:
                dfs(r,COLS-1)
        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0,c)
            if board[0][c]:
                dfs(ROWS-1,c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'        