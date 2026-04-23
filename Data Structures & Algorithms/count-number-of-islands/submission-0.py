class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        bool_grid = ([[False] * cols for _ in range(rows)])
        ctr = 0
        direction = [[1,0], [-1,0], [0,1], [0,-1]]

        def bfs(row,col):
            q = collections.deque()
            q.append((row, col))
            while q:
                row, col = q.popleft()
                for dr, dc in direction:
                    x = dr+ row
                    y = dc +col
                    if x in range(rows) and y in range(cols) and grid[x][y] != "0" and bool_grid[x][y] != True:
                        q.append((x,y))
                        bool_grid[x][y] = True

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != "0" and bool_grid[row][col] != True:
                    bool_grid [row][col] = True
                    bfs(row, col)
                    ctr +=1

        return ctr