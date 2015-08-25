class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, bool> visited;

        for (int i = 0; i < nums.size(); ++i) {
            if (visited.count(nums[i])) {
                return true;
            }
            visited[nums[i]] = true;
        }

        return false;
    }
};
