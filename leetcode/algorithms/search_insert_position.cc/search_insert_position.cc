class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int n = nums.size();

        int left = 0;
        int right = n - 1;

        while (left < right) {
            int mid = left/2 + right/2;
            if (nums[mid] >= target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        if (right == n - 1 && nums[right] < target) {
            ++right;
        }
        return right;
    }
};
