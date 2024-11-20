class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstringLength = 0
        visited = set()
        left, right = 0, 0
        while right < len(s):
            cur = s[right]

            while cur in visited:
                visited.remove(s[left])
                left += 1
            visited.add(cur)
            longestSubstringLength = max(longestSubstringLength, len(s[left : right + 1]))
            right += 1
        
        return longestSubstringLength

"""
1. Naive Solution O(n^2)

Nested for loop. Find every possible substring. For each substring, check whether there are duplicates (How?). If there are none, then update the max length. otherwise, ignore.

2. Optimized Solution.

Sliding Window.

s = "abcabcbb"
      ^
        ^

longestSubstringLength = 0
visitedSet = {}
left, right = 0
while right < len(s):
    cur = s[right]
    while cur in visitedSet:
        visitedSet.remove(s[left])
        left += 1
    longestSubstringLength = max(longestSubstringLength, len(s[left:right + 1]))
    right += 1
    
return longestSubstringLength

Key idea, we make use of a sliding window.

We progress right until we find duplicate character. Then we progress left to eliminate duplicates. We track the longest substring length that has no duplicates. At each step, after we have made a substring between the sliding window that has no duplicates, we then update the longest substring length that we are going to be tracking.

At the end, we return the longest substring length that has no duplicates.

"""
