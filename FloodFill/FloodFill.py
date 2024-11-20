class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initialColor = image[sr][sc]
        m, n = len(image), len(image[0])

        deltas = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def recurse(row, col):
            # Base Case
            if image[row][col] == color:
                return

            # Recursive Case
            image[row][col] = color

            for delta in deltas:
                newRow = row + delta[0]
                newCol = col + delta[1]
                
                if newRow < 0 or newRow > m - 1 or newCol < 0 or newCol > n - 1:
                    continue
                
                if image[newRow][newCol] == initialColor:
                    recurse(newRow, newCol)
        
        recurse(sr, sc)

        return image

