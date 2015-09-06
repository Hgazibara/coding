class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int total_max = nums[0];
        int current_max = nums[0];

        for (int i = 1; i < nums.size(); ++i) {
            current_max = max(nums[i], nums[i] + current_max);
            total_max = max(current_max, total_max);
        }

        return total_max;
    }
};
