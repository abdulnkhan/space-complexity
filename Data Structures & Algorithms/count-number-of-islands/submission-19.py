class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        bfs with visit set 
        in bfs i'll check all directions where a 1 can exist -> add it to the visit set
        """
        if grid == []:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])


        def bfs(row, col):
            q = deque()
            dirs = [[0,1], [1,0], [0,-1], [-1,0]]

            q.append([row,col])

            while q:
                row, col = q.popleft()

                for dr, dc in dirs:
                    r = dr + row
                    c = dc + col

                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1' and (r,c) not in visit:
                        q.append([r,c])
                        visit.add((r,c))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row,col) not in visit:
                    bfs(row,col)
                    islands += 1

        return islands