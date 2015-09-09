class Solution {
public:
    string multiply(string num1, string num2) {
        deque<int> result;

        int m = num1.size();
        int n = num2.size();

        for (int j = 0; j < n; ++j) {
            if (j == 0) {
                int carry = 0;

                for (int i = m - 1; i >= 0; --i) {
                    int temp = (num1[i] - '0') * (num2[j] - '0') + carry;
                    carry = (temp - temp % 10) / 10;
                    result.push_front(temp % 10);
                }

                while (carry) {
                    result.push_front(carry % 10);
                    carry /= 10;
                }
            } else {
                result.push_back(0);

                int carry = 0;
                int pos = result.size() - 1;

                for (int i = m - 1; i >= 0; --i) {
                    int temp = (num1[i] - '0') * (num2[j] - '0') + carry + result[pos];
                    carry = (temp - temp % 10) / 10;
                    result[pos--] = temp % 10;
                }

                while (carry) {
                    result.push_front(carry % 10);
                    carry /= 10;
                }
            }
        }

        stringstream str_result;
        copy(result.begin(), result.end(), ostream_iterator<int>(str_result, ""));

        return str_result.str();
    }
};
