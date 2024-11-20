class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        finalIntervals = []
        n = len(intervals)
        i = 0

        while i < n and intervals[i][1] < newInterval[0]:
            finalIntervals.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        
        finalIntervals.append(newInterval)

        while i < n:
            finalIntervals.append(intervals[i])
            i += 1
        
        return finalIntervals

"""

intervals = [
    [1, 2], [3, 5], [6, 7], [8, 10], [12, 16]
]

newInterval = [4, 8]

final = []
cur = [1, 2]
newInterval = [4, 8]

if cur[0] < newInterval[0] or cur[0] : # expand the newInterval



"""
