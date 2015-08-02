#include <iostream>
#include <vector>
#include <utility>

bool is_prime(int number) {
    return false;
}

int main(void) {
    int T;
    std::cin >> T;

    while (T > 0) {
        int M, N;
        std::cin >> M >> N;

        for (int i = M; i <= N; i++) {
            if (is_prime(i)) {
                std::cout << i << std::endl;
            }
        }
    }

    return 0;
}
