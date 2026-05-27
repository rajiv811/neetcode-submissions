class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        This is NOT a path problem. This is a wave problem, difference
        being that you can multiple points (rotten) where it can start.
        Path assumes one start location. Use BFS
        """
        ROWS,COLS = len(grid), len(grid[0])
        fresh = 0
        rotten = collections.deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rotten.append((r,c))    
        # BFS
        time = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while fresh > 0 and rotten:
            length = len(rotten)
            for i in range(length):
                r,c = rotten.popleft()

                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1:
                        continue
                    else:
                        grid[nr][nc] = 2
                        rotten.append((nr,nc))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1




        

