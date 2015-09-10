class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        map<long long, int> indexes;
        vector<string> numbers;

        if (numerator == 0 || denominator == 0) {
            return "0";
        }

        int sign = 1;

        if ((numerator < 0 && denominator > 0) || (numerator > 0 && denominator < 0)) {
            sign = -1;
        }

        long long num = abs(numerator);
        long long denom = abs(denominator);

        int start_repetition = -1;
        int index = 0;

        while (numerator > 0) {
            long long quotient = num / denom;
            numbers.push_back(to_string(quotient > 0 ? quotient : -quotient));

            long long remainder = num % denom;

            if (remainder == 0) {
                break;
            }

            if (indexes.count(remainder)) {
                start_repetition = indexes[remainder];
                break;
            }

            indexes[remainder] = index++;
            num = remainder * 10;
        }

        string result;

        if (numbers.size() == 1) {
            result = numbers[0];
        } else if (start_repetition == -1) {
            result = numbers[0] + "." + convert(numbers.begin() + 1, numbers.end());
        } else {
            string whole = numbers[0] + ".";
            string not_repeated = convert(numbers.begin() + 1, numbers.begin() + start_repetition + 1);
            string repeated = "(" + convert(numbers.begin() + start_repetition + 1, numbers.end()) + ")";
            result = whole  + not_repeated + repeated;
        }

        return sign > 0 ? result : "-" + result;
    }

    string convert(vector<string>::iterator start, vector<string>::iterator end) {
        stringstream str_result;
        copy(start, end, ostream_iterator<string>(str_result, ""));
        return str_result.str();
    }
};
