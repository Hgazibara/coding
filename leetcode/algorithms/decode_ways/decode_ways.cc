class Solution {
public:
    int numDecodings(string s) {
        if (s.empty() || s == "0" || s[0] == '0') {
            return 0;
        }

        int n = s.size();
        vector<int> ways(n, 0);

        ways[0] = 1;
        ways[1] = s[1] != '0' ? 1 : 0;

        if (isValid(s.substr(0, 2))) {
            ++ways[1];
        }

        for (int i = 2; i < n; ++i) {
            if (s[i] != '0') {
                ways[i] = ways[i - 1];
            }

            if (isValid(s.substr(i - 1, 2))) {
                ways[i] += ways[i - 2];
            }
        }

        return ways[n - 1];
    }

    bool isValid(string s) {
        int number = stoi(s);
        return number >= 10 && number <= 26;
    }
};
