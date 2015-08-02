#include <iostream>
#include <vector>

int calculate(int k, int n) {
    std::vector<std::vector<int>> sums(k + 1, std::vector<int>(n + 1, 0));

    for (int i = 0; i <= n; ++i) {
        sums[0][i] = i;
    }

    for (int i = 1; i <= k; ++i) {
        for (int j = 1; j <= n; ++j) {
            for (int l = 1; l <= j; ++l) {
                sums[i][j] += sums[i - 1][l];
            }
        }
    }

    return sums[k][n];
}

int main(void) {
    int k, n;

    std::cin >> k;
    std::cin >> n;

    std::cout << calculate(k, n) << std::endl;

    return 0;
}
