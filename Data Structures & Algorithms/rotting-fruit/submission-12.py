class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        prework: count fresh, append q
        """
        fresh = 0
        q = deque()
        t = 0
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue
                elif grid[row][col] == 1:
                    fresh += 1
                else:
                    q.append([row,col])
                

        dirs = [[0,1],[1,0],[0,-1],[-1,0]]

        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in dirs:
                    r = row + dr
                    c = col + dc

                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append([r,c])
                        fresh -= 1

            t += 1

        return t if fresh == 0 else -1