class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        go through grid -> as soon as we find a 1 we're going to do a BFS to find all other parts of that same island

        visit = set((row,col))

        """
        if grid == []:
            return 0

        numIslands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col):
            q = deque([])
            visit.add((row,col))
            q.append([row,col])
            dirs = [[1,0], [0,1], [-1,0], [0,-1]]

            while q:
                row, col = q.popleft()

                for dr, dc in dirs:
                   r = row + dr
                   c = col + dc
                   if not (0 <= r < rows and 0 <= c < cols and grid[r][c] == '1' and (r,c) not in visit):
                        continue
                    
                   q.append([r,c])
                   visit.add((r,c))
                
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row,col) not in visit:
                    bfs(row,col)
                    numIslands += 1

        return numIslands
