import collections

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []
        nums.sort()

        # use each possible number in the input array as a possible first value.
        for i, value in enumerate(nums):
            # we don't want to reuse the same value in the same position twice.
            if i > 0 and value == nums[i - 1]:
                continue
            
            # we use essentially solve two sum using two pointers here in a sorted array.
            l, r = i + 1, n - 1

            while l < r:
                threeSum = value + nums[l] + nums[r]

                # exploit sorted property, if > 0, then we need to decrease the value of the sum.
                # to do this, we make the value less positive by adding a less positive value and
                # shifting the right pointer left. (less positive, since sorted array)
                if threeSum > 0:
                    r -= 1
                # exploit sorted property, if < 0, then we need to increase the value of the sum.
                # to do this, we make the value more positive by adding a more positive value while
                # still staying within the range of the array and we shift the left pointer right.
                # (more positive, since sorted array)
                elif threeSum < 0:
                    l += 1
                # otherwise, it is equal to 0. then we add the triplet to the res array. then we need
                # to progress the left pointer only and not the right pointer. why? because the first value
                # i is shifting right, then we only need to shift the left pointer right to change the
                # window that we use to do the two sum on the remaining elements. then, we use a while loop
                # to increment the left pointer until it is no longer a duplicate of previous element.
                else:
                    res.append([value, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res


"""

2. Optimized Solution

What can we do to optimize now that we have figured out the brute force solution?

So the optimized solution looks like this.

"""

"""

Given an integer array, return all the triplets of the form [nums[i], nums[j], nums[k]] such that i != j, i != k and j != k and such that nums[i] + nums[j] + nums[k] == 0. Solution set cannot contain duplicate triplets.

1. Naive Solution O(n^3)

Triple for loop. i runs from 0 to n - 1. j runs from 0 to n - 1 excluding i. k runs from 0 to n - 1 excluding i and j. Then what's the condition?

The problem is eliminating the duplicates.

if nums[i] + nums[j] + nums[k] == 0, we want to add this triplet to the set of triplets. Now, the problem with this is that it creates the possibility of duplicates. Sort the array first so let's try to solve it using the sorting.

So we have a workable brute force solution. Now to optimise.
Class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        i = 0
        res = []
        nums.sort()

        for i in range(0, n):
            for j in range(0, n):
                if j == i:
                    continue
                for k in range(0, n):
                    if k == i or k == j:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        if [nums[i], nums[j], nums[k]] in res or [nums[i], nums[k], nums[j]] in res or [nums[j], nums[i], nums[k]] in res or [nums[j], nums[k], nums[i]] in res or [nums[k], nums[i], nums[j]] in res or [nums[k], nums[j], nums[i]] in res:
                           continue
                        
                        res.append([nums[i], nums[j], nums[k]])
        
        return res

"""
