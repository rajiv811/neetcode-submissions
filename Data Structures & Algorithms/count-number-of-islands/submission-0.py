class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    self.dfs(grid,r,c)
                    count += 1
        return count
        
    def dfs(self, grid,x,y):
        # cases
        if  x < 0 or y < 0 or x > len(grid)-1 or y > len(grid[0])-1 or grid[x][y] != '1':
            return

        grid[x][y] = '#'
        self.dfs(grid,x-1,y)
        self.dfs(grid,x+1,y)
        self.dfs(grid,x,y-1)
        self.dfs(grid,x,y+1)
        