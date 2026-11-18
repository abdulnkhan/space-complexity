class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0 

        islands = 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        def bfs(row, col):
            q = deque()
            q.append([row,col])
            dirs = [[0,1], [1,0], [0,-1], [-1,0]]

            while q:
                row, col = q.popleft()

                for dr, dc in dirs:
                    r = row + dr
                    c = col + dc

                    if not (0 <= r < rows and 0 <= c < cols and (r,c) not in visit and grid[r][c] == '1'):
                        continue

                    q.append([r,c])
                    visit.add((r,c))



        for row in range(rows):
            for col in range(cols):
                if (row,col) not in visit and grid[row][col] == '1':
                    bfs(row,col)
                    islands += 1

        return islands