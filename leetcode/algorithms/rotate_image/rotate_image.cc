class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int lower = 0;
        int upper = n - 1;

        while (lower < upper) {
            int m = upper - lower;

            for (int i = 0; i < m; ++i) {
                int temp = matrix[lower][lower + i];

                matrix[lower][lower + i] = matrix[upper - i][lower];
                matrix[upper - i][lower] = matrix[upper][upper - i];
                matrix[upper][upper - i] = matrix[lower + i][upper];

                matrix[lower + i][upper] = temp;
            }
            ++lower;
            --upper;
        }
    }
};
