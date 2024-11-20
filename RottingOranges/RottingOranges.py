class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        deltas = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]

        m, n = len(grid), len(grid[0])

        maxTime = 0

        queue = []
        numOranges = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 2:
                    queue.append(( i, j, 0 ))
                if grid[i][j] != 0:
                    numOranges += 1

        while queue:
            print(queue)
            row, col, time = queue.pop(0)
            maxTime = max(time, maxTime)

            for change_row, change_col in deltas:
                new_row, new_col = row + change_row, col + change_col
                
                if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n:
                    continue
                
                if grid[new_row][new_col] == 1:
                    queue.append(( new_row, new_col, time + 1 ))
                    grid[new_row][new_col] = 2
        
        numberOfRottenOranges = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 2:
                    numberOfRottenOranges += 1

        return maxTime if numOranges == numberOfRottenOranges else -1



"""



"""
