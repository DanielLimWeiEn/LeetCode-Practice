class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

"""
So, easiest way to do this is using python, len(set(nums)) != len(nums)
"""
