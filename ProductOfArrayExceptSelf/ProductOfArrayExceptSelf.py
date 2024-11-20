class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixMult = [0] * n
        suffixMult = [0] * n
        res = [0] * n

        prefixMultValue = 1
        for i in range(0, n):
            prefixMult[i] = prefixMultValue * nums[i]
            prefixMultValue = prefixMult[i]
        
        suffixMultValue = 1
        for i in range(n - 1, -1, -1):
            suffixMult[i] = suffixMultValue * nums[i]
            suffixMultValue = suffixMult[i]
        
        for i in range(0, n):
            if i == 0:
                res[i] = suffixMult[i + 1]
            elif i == n - 1:
                res[i] = prefixMult[i - 1]
            else:
                res[i] = suffixMult[i + 1] * prefixMult[i - 1]
        
        return res

"""

nums = [1, 2, 3, 4]
preMult = [1, 2, 6, 24]
postMult = [24, 24, 12, 4]
res = [

]

"""