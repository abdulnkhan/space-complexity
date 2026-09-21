class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        I need to traverse the grid until i find a 1 - once i have that one then i just perform a bfs and increment islands + 1
        To avoid double counting we will make sure that key doesnt exist in the visit set that we have
        """

        if grid == []:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0
        visit = set()

        def bfs(row, col):
            directions = [[0,1], [1,0], [0, -1], [-1,0]]
            q = deque([[row,col]])
            visit.add((row, col))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if (0 <= r < rows) and (0 <= c < cols) and (r,c) not in visit and grid[r][c] == '1':
                        q.append([r,c])
                        visit.add((r,c))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands
