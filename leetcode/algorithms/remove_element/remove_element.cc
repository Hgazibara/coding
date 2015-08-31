class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int insert_position = 0;
        int n = nums.size();

        for (int i = 0; i < n; ++i) {
            if (nums[i] != val) {
                nums[insert_position++] = nums[i];
            }
        }

        return insert_position;
    }
};
