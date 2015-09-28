class Solution {
public:
    int numDistinct(string s, string t) {
        int m = s.size();
        int n = t.size();

        vector<vector<int>> counts(m + 1, vector<int>(n + 1, 0));

        for (int i = 0; i < m; ++i) {
            counts[i][0] = 1;
        }

        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                counts[i][j] += counts[i - 1][j];
                if (s[i - 1] == t[j - 1]) {
                    counts[i][j] += counts[i - 1][j - 1];
                }
            }
        }

        return counts[m][n];
    }
};
