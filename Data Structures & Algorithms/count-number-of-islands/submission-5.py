class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        traverse through rows and cols in grid
        when i find a 1 i need to do BFS to find all adjacent 1's
            inside the bfs we will just check all dirs and go from there
        """
        if grid == []:
            return 0         
        islands = 0
        visit = set()

        rows, cols = len(grid), len(grid[0])

        def bfs(row, col):
            direction = [[0,1], [1,0], [0,-1], [-1,0]]
            q = deque([[row, col]])
            visit.add((row,col))

            while q:
                row, col = q.popleft()

                for dr, dc in direction:
                    r = row + dr
                    c = col + dc

                    if (0 <= r < rows) and (0 <= c < cols) and ((r,c) not in visit) and (grid[r][c] == '1'):
                        q.append([r,c])
                        visit.add((r,c))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row,col) not in visit:
                    bfs(row, col)
                    islands += 1

        return islands

