class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def bfs(r,c):
            q = deque([(r,c)])
            visited = set()
            visited.add((r,c))
            steps = 0
            while q:
                for i in range(len(q)):
                    row,col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dr,dc in directions:
                        nr,nc = row + dr, col + dc
                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != -1 and (nr,nc) not in visited:
                            q.append((nr,nc))
                            visited.add((nr,nc))
                steps += 1
            return 2147483647
  
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2147483647:
                    grid[i][j] = bfs(i,j)            


