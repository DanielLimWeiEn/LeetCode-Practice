function twoSum(nums: number[], target: number): number[] {
    const map = {};

    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];

        if (nums[i] in map) {
            return [map[nums[i]], i];
        }

        map[complement] = i;
    }
};
