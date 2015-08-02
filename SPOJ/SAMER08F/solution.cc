#include <iostream>

int main(void) {
    int N;
    std::cin >> N;

    while (N != 0) {
        std::cout << N * (N+1) * (2*N + 1) / 6 << std::endl;
        std::cin >> N;
    }

    return 0;
}
