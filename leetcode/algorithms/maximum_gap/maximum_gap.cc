class Solution {
public:
    int maximumGap(vector<int>& nums) {
        int n = nums.size();

        if (n < 2) {
            return 0;
        }

        int min_value = *min_element(nums.begin(), nums.end());
        int max_value = *max_element(nums.begin(), nums.end());

        int gap = (max_value - min_value - 1) / (n - 1) + 1;

        if (gap == 0) {
            return 0;
        }

        vector<pair<int, int>> buckets(n, make_pair(INT_MAX, INT_MIN));

        for (int &value: nums) {
            int bucket = (value - min_value) / gap;

            int bucket_min = min(buckets[bucket].first, value);
            int bucket_max = max(buckets[bucket].second, value);

            buckets[bucket] = make_pair(bucket_min, bucket_max);
        }

        int max_gap = INT_MIN;
        int prev = min_value;

        for (pair<int, int> &bucket: buckets) {
            if (bucket.first == INT_MAX && bucket.second == INT_MIN) {
                continue;
            }

            max_gap = max(max_gap, bucket.first - prev);
            prev = bucket.second;
        }

        return max_gap;
    }
};
