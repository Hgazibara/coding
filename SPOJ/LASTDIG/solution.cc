#include <iostream>

int last_digit(int a, int b) {
    if (b == 0) {
        return 1;
    }
    if (b == 1) {
        return a % 10;
    }
    if (b % 2 == 0) {
        return (last_digit(a, b/2) % 10 * last_digit(a, b/2) % 10) % 10;
    } else {
        return (last_digit(a, b/2) % 10 * last_digit(a, b - b/2) % 10) % 10;
    }
}

int main(void) {
    int T;
    std::cin >> T;

    while (T > 0) {
        int a, b;
        std::cin >> a >> b;
        std::cout << last_digit(a, b) << std::endl;
        T--;
    }

    return 0;
}
