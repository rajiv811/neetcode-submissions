class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        def isIsland(x,y):
            if x < 0 or y < 0 or x >= ROWS or y >= COLS or grid[x][y] != 1:
                return 0
            grid[x][y] = '#'
            return 1 + isIsland(x+1,y) + isIsland(x-1,y) + isIsland(x,y+1) + isIsland(x,y-1)

        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, isIsland(r,c))
        
        return max_area
