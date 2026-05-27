class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = self.dfs(grid,r,c)
                    max_area = max(max_area,area)
        return max_area
    def dfs(self,grid,x,y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
            return 0
        grid[x][y] = 0
        return (1 + self.dfs(grid,x+1,y) + 
                self.dfs(grid,x-1,y) + 
                self.dfs(grid,x,y+1) + 
                self.dfs(grid,x,y-1))

        