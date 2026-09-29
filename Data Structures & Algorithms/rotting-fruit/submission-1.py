class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh, time = 0, 0
        rows, cols = len(grid), len(grid[0])
        #First we do prework and count all fresh and populate q with all rotten

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append([row,col])

        dirs = [[0,1], [1,0], [0,-1], [-1,0]]

        while q and fresh > 0:
            
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in dirs:
                    r = row + dr
                    c = col + dc

                    if not(0 <= r < rows and 0 <= c < cols and grid[r][c] == 1):
                        continue
                    grid[r][c] = 2
                    fresh -= 1
                    q.append([r,c])
            time += 1

        return time if fresh == 0 else -1