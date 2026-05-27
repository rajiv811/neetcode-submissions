class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        0 - empty
        1 - fresh
        2 - rotten

        Initial Thought Process:
        Find rotten fruit
        Since we need MINIMUM time --> BFS
        1. Gather all rotten fruit into a queue
        2. Run BFS on the queue
        """
        q = deque()
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        time = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r,c = q.popleft()
                for d in directions:
                    nr,nc = r+d[0],c+d[1]
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1


                
