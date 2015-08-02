#include <iostream>
#include <vector>

void propagate(std::vector<int>& digits, int j, int overflow) {
    if (overflow == 0) {
        return;
    }

    if (j + 1 < digits.size()) {
        int result = digits[j + 1] + overflow;
        digits[j + 1] = result % 10;
        propagate(digits, j + 1, result / 10);
    } else {
        digits.push_back(overflow);
    }
}

std::vector<int> fact(int n) {
    std::vector<int> digits; 
    digits.push_back(1);

    for (int i = 2; i <= n; ++i) {
        for (int j = digits.size() - 1; j >= 0; --j) {
            int result = digits[j] * i;
            digits[j] = result % 10;
            propagate(digits, j, result / 10);
        }
    }

    return digits;
}

void print_digits(std::vector<int> digits) {
    for (auto it = digits.rbegin(); it != digits.rend(); ++it) {
        std::cout << *it;
    }
    std::cout << std::endl;
}


int main(void) {
    int T;
    std::cin >> T;

    while (T > 0) {
        int n;

        std::cin >> n;
        auto digits = fact(n);
        print_digits(digits);

        --T;
    }

    return 0;
}
