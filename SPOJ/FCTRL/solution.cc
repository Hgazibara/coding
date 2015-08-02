#include <iostream>
#include <cmath>

int main(void) {
    int T;
    std::cin >> T;

    while (T > 0) {
        int N;
        std::cin >> N;

        int p = 1;
        int zeros = 0;
        int denominator = (int)std::pow(5, p);

        while (denominator <= N) {
            zeros += N/denominator;
            ++p;
            denominator = (int)std::pow(5, p);
        }

        std::cout << zeros << std::endl;
        --T;
    }

    return 0;
}
