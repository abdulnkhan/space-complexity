class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        prework

        """
        if grid == []:
            return -1

        fresh = 0
        q = deque()
        rows, cols = len(grid), len(grid[0])
        t = 0
        # prework - count fresh and populate q
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

                    if not (0 <= r < rows and 0 <= c < cols and grid[r][c] == 1):
                        continue
                    
                    q.append([r,c])
                    grid[r][c] = 2
                    fresh -= 1
            t += 1

        return t if fresh ==0 else -1


    