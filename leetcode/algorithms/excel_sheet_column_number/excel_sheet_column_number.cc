class Solution {
public:
    int titleToNumber(string s) {
        int column_number = 0;
        int power = 1;

        for (int i = s.size() - 1; i >= 0; --i) {
            column_number += (s[i] - 'A' + 1) * power;
            power *= 26;
        }

        return column_number;
    }
};
