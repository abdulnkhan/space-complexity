class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        prework: count all fresh, map all rotten in a q, create a variable with time, visit set to make sure a rotten fruit is not marked yet

        we're going to do BFS consecutively of all the rotten fruits and make sure we mark it rotten - at each BFS level we will increment the time
        """

        q = deque()
        t = 0
        fresh = 0

        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue
                if grid[row][col] == 1:
                    fresh += 1
                else:
                    q.append([row,col])

        dirs = [[0,1],[1,0], [0,-1], [-1,0]]
        
        while q and fresh > 0:
            for _ in range(len(q)):
                row,col = q.popleft()

                for dr, dc in dirs:
                    r = row + dr
                    c = col + dc

                    if not(0 <= r < rows and 0 <= c < cols and grid[r][c] == 1):
                        continue
                    q.append([r,c])
                    grid[r][c] = 2
                    fresh -= 1
            t += 1

        return t if fresh == 0 else -1