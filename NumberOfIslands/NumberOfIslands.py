class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        deltas = [
            [0, -1],
            [0, 1],
            [-1, 0],
            [1, 0]
        ]

        m, n = len(grid), len(grid[0])
        visited = set()

        islands = 0
        def dfs(row, col):
            if (row, col) in visited:
                return

            visited.add((row, col))

            for x_change, y_change in deltas:
                new_row, new_col = row + x_change, col + y_change
                if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n:
                    continue
                if grid[new_row][new_col] == "1":
                    dfs(new_row, new_col)
        
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    islands += 1
                    dfs(i, j)
        return islands

"""

ok, so this particular problem. yes I've done it before and yes I should know how to do it. so I will try it and see how it goes?

what do I have to do first?

1. created a visited set or grid.
2. define a dfs algorithm.
3. count for the number of islands.
4. define deltas.

"""
