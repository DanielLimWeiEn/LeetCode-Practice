class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSumEndingAtElement = len(nums) * [float('-inf')]
        maxSubArraySum = float('-inf')

        if len(nums) == 1:
            return nums[0]

        for i in range(0, len(nums)):
            if i == 0:
                maxSumEndingAtElement[i] = nums[i]
            else:
                maxSumEndingAtElement[i] = max(maxSumEndingAtElement[i - 1] + nums[i], nums[i])
            maxSubArraySum = max(maxSubArraySum, maxSumEndingAtElement[i])
        
        return maxSubArraySum

"""
1. Naive Approach O(n^2) runtime

Consider every possible window using a double for loop.

maxSum = float('-inf')
for i in range(0, len(nums)):
    curSum = 0
    for j in range(i, len(nums)):
        curSum += nums[j]
        maxSum = max(maxSum, curSum)
return maxSum

So the naive approach works. Now can we do better.

2. Smarter Approach O(n) runtime

Use Kadane's algorithm.

Idea: 2 array traversals

1st -> each i marks the maximum subarray sum starting at any element before this and ending at this ith element.
maxEnding[i] = max(maxEnding[i - 1] + arr[i], arr[i])
At each ith element, there are 2 choices. First, the maximum subarray sum ending at the previous element is positive, in which case it is always better to add the current element onto that. Second, the maximum subarray sum ending at the previous element is negative, in which case it is always better to start the sum from afresh, i.e. just arr[i].

2nd -> find the max of those values as our answer.

"""
