class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        for i in range(0, m):
            for j in range(0, n):
                if mat[i][j] == 0:
                    mat[i][j] = 0
                else:
                    left = mat[i - 1][j] if i > 0 else math.inf
                    up = mat[i][j - 1] if j > 0 else math.inf
                    mat[i][j] = 1 + min(left, up)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 0:
                    mat[i][j] = 0
                else:
                    right = mat[i + 1][j] if i < m - 1 else math.inf
                    down = mat[i][j + 1] if j < n - 1 else math.inf
                    mat[i][j] = min(mat[i][j], right + 1, down + 1)
        
        return mat

"""
mat = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]

idea:
the idea makes use of dynamic programming.

- for '0' marked cells, define distance of nearest '0' as 0, since the cell itself is a '0'.
- for '1' marked cells, define distance of nearest '0' as the following: 1 + distance of nearest '0' to any of the 4 surrounding cells. mat[i][j].

1 + min(
    distance of nearest '0' to mat[i - 1][j], # left
    distance of nearest '0' to mat[i][j - 1], # up
    distance of nearest '0' to mat[i + 1][j], # right
    distance of nearest '0' to mat[i][j + 1], # down
)

BUT, using 1 iteration, that isn't possible. With DP, the assumption is that the 4 surrounding distances have to have been calculated already. But they are not.

- So we split it up. First, we consider LEFT and UP only as we do the first iteration from top down.
- Then we consider BOTTOM and RIGHT only as we do the second iteration from bottom up.

On first iteration, we consider the distance = 1 + min(LEFT, UP) as we move left to right and up to down.
On second iteration, we consider the distance = min(RIGHT + 1, BOTTOM + 1, current = 1 + min(LEFT, UP)) as we move right to left and bottom to up. Essentially, we do the same dynamic programming, except in steps.

"""
