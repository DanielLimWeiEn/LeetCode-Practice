# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            m = int(l + ((r - l) / 2))

            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1
        
        return int(l)
# essentially make use of binary search and the invariant that
# if you check the mid, if it's bad, you go left, else, you go right
# 1 2 3 4 5
# l   m   r
# 1 + (5 - 1) / 2 = 3
# 1 2
# l r
# m = 1 + 1/2