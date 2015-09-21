class Solution {
public:
    string getPermutation(int n, int k) {
        vector<string> result(n, "");

        vector<int> factorials = computeFactorials(n);
        vector<int> digits = getDigits(n);

        int p = n - 1;
        --k;

        for (int i = 0; i < n; ++i) {
            int pos = k / factorials[p];
            result[i] = to_string(digits[pos]);
            digits.erase(digits.begin() + pos);
            k %= factorials[p];
            --p;
        }

        stringstream str_result;
        copy(result.begin(), result.end(), ostream_iterator<string>(str_result, ""));

        return str_result.str();
    }

    vector<int> computeFactorials(int n) {
        vector<int> factorials(n + 1, 1);

        for (int i = 2; i <= n; ++i) {
            factorials[i] *= factorials[i - 1] * i;
        }

        return factorials;
    }

    vector<int> getDigits(int n) {
        vector<int> digits;

        for (int i = 1; i <= n; ++i) {
            digits.push_back(i);
        }

        return digits;
    }
};
