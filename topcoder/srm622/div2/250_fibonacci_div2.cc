#include <iostream>
#include <algorithm>
#include <cmath>

int find(int N) {
    int prev = 0;
    int curr = 1;

    while (curr <= N) {
        int temp = prev;
        prev = curr;
        curr = curr + temp;
    }

    return std::min(std::abs(N - prev), std::abs(N - curr));
}

int main(void) {
    int T;
    std::cin >> T;

    for (int i = 0; i < T; ++i) {
        int N;
        std::cin >> N;
        std::cout << find(N) << std::endl;
    }

    return 0;
}
