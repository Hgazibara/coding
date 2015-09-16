class Solution {
public:
    int longestValidParentheses(string s) {
        int longest_substring_length = 0;
        int n = s.size();

        vector<int> lengths(n, 0);

        for (int i = 1; i < n; ++i) {
            if (s[i] == ')') {
                if (s[i - 1] == '(') {
                    lengths[i] = 2;
                    if (i >= 2) {
                        lengths[i] += lengths[i - 2];
                    }
                } else {
                    int length = lengths[i - 1];
                    int j = i - length - 1;

                    if (j < 0 || s[j] != '(') {
                        continue;
                    }

                    lengths[i] = lengths[i - 1] + 2;

                    if (j > 0) {
                        lengths[i] += lengths[j - 1];
                    }
                }
            }
            longest_substring_length = max(longest_substring_length, lengths[i]);
        }

        return longest_substring_length;
    }
};
