#include <iostream>
#include <algorithm>
#include <vector>

int maxTurns(std::vector<int> cards) {
    std::sort(cards.begin(), cards.end());

    int result = 0;
    int block_size = 0;

    for (int i = 0; i < cards.size(); ++i) {
        int last_block = 0;

        if (i == 0 || cards[i] == cards[i - 1] + 1) {
            ++block_size;
        } else {
            last_block = block_size;
            block_size = 1;
        }

        result += (last_block + 1)/2;

        if (i == cards.size() - 1) {
            result += (block_size + 1) / 2;
        }
    }

    return result;
}

int main(void) {
    int N;
    std::cin >> N;

    std::vector<int> cards(N, 0);

    for (int i = 0; i < N; ++i) {
        std::cin >> cards[i];
    }

    std::cout << maxTurns(cards) << std::endl;

    return 0;
}
