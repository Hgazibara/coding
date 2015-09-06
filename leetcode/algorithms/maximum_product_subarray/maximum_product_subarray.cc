class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int current_min = nums[0];
        int current_max = nums[0];
        int total_max = nums[0];

        for (int i = 1; i < nums.size(); ++i) {
            int value = nums[i];
            int max_here = current_max;
            int min_here = current_min;

            current_min = min(min(max_here*value, min_here*value), value);
            current_max = max(max(max_here*value, min_here*value), value);

            total_max = max(current_max, total_max);
        }

        return total_max;
    }
};
