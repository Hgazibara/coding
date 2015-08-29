class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();

        vector<int> result;
        map<int, int> positions;

        for (int i = 0; i < n; ++i) {
            int x = nums[i];
            int y = target - x;

            if (positions.count(y)) {
                result.push_back(positions[y]);
                result.push_back(i + 1);
                return result;
            }

            positions[x] = i + 1;
        }

        return result;
    }
};
