class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for point in points:
            point.append(math.sqrt(pow(point[0], 2) + pow(point[1], 2)))
        
        points.sort(key=lambda point : point[2])
        return list(map(lambda point : point[:2], points[:k]))

"""
1. Naive Solution.

- go through points, calculate each distance.
- sort by distance.
- return the top k.

Time: O(n log n)

2. Faster Sulution.

"""
