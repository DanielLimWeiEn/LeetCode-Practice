class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        mapping = {}

        for num in nums:
            if num not in mapping:
                mapping[num] = 0
            mapping[num] += 1
        
        for num in mapping.keys():
            if mapping[num] > int(n / 2):
                return num

        # majority_element = 0
        # majority_element_count = 0

        # for num in nums:
        #     if majority_element_count == 0:
        #         majority_element = num
        #         majority_element_count = 1
        #     else:
        #         if num == majority_element:
        #             majority_element_count += 1
        #         elif num != majority_element:
        #             majority_element_count -= 1
        
        # return majority_element


"""
let's think of a non-optimal O(n) and then O(n) space solution.

mapping = {
    number : count
}

Ok so the above solution has been coded. The question is how do I do better? Space-wise how do I use O(1) space?
majority_element
majority_element_count

then find the one with the maximum count and that is the majority element.

is there any invariant or important fact that I can exploit to solve this question?

I know for a fact that the majority element ALWAYS exists + it appears more than [n / 2] times.


"""
