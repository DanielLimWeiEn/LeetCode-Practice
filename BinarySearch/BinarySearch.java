class Solution {
    public int search(int[] nums, int target) {
        int l = 0; int r = nums.length - 1;

        while (r >= l) {
            int mid = l + (r - l) / 2;

            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                r = mid - 1;
                continue;
            } else if (nums[mid] < target) {
                l = mid + 1;
                continue;
            }
        }

        return -1;
    }
}
