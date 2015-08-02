#include <iostream>

int main(void) {
    int N;
    std::cin >> N;

    for (; N > 0; --N) {
        int x, y;
        std::cin >> x >> y;

        if (x == y || y == x - 2) {
            std::cout << (x % 2 == 0 ? x + y : x + y - 1) << std::endl;
        } else {
            std::cout << "No Number" << std::endl;
        }
    }

    return 0;
}
