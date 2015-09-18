class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        if (s1.size() + s2.size() != s3.size()) {
            return false;
        }

        if (s1.size() == 0 && s2.size() == 0) {
            return true;
        }

        int m = s1.size();
        int n = s2.size();

        vector<vector<bool>> checks(m + 1, vector<bool>(n + 1, false));
        checks[0][0] = true;

        for (int i = 1; i <= m; ++i) {
            checks[i][0] = checks[i - 1][0] && s1[i - 1] == s3[i - 1];
        }

        for (int j = 1; j <= n; ++j) {
            checks[0][j] = checks[0][j - 1] && s2[j - 1] == s3[j - 1];
        }

        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                bool can_use_s1 = checks[i - 1][j] && s1[i - 1] == s3[i + j - 1];
                bool can_use_s2 = checks[i][j - 1] && s2[j - 1] == s3[i + j - 1];
                checks[i][j] = can_use_s1 || can_use_s2;
            }
        }

        return checks[m][n];
    }
};
