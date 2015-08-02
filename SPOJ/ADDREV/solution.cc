#include <algorithm>
#include <iostream>
#include <string>
#include <cmath>

int to_reversed_int(std::string a) {
    int len = a.size();
    int result = 0;

    while (len > 0) {
        result += (a[len - 1] - '0') * (int)std::pow(10, len - 1);
        --len;
    }

    return result;
}

int main(void) {
    int N;
    std::cin >> N;

    while (N > 0) {
        std::string a, b;
        std::cin >> a >> b;

        int ra = to_reversed_int(a);
        int rb = to_reversed_int(b);
        std::cout << to_reversed_int(std::to_string(ra + rb)) << std::endl;

        --N;
    }

    return 0;
}
