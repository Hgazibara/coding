#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>

class ChessFloor {
public:
    int minimumChanges(std::vector<std::string> floor) {
        int n = floor.size();
        int changes = 0;

        char color_a = this->find_color(floor, 0, 0);
        char color_b = this->find_color(floor, 1, color_a);

        for (int i = 0; i < n; ++i) {
            int first_color = i % 2 == 0 ? color_a : color_b;
            int second_color = i % 2 == 1 ? color_a : color_b;

            for (int j = 0; j < n; ++j) {
                if (j % 2 == 0 && floor[i][j] != first_color) {
                    ++changes;
                } else if (j % 2 == 1 && floor[i][j] != second_color) {
                    ++changes;
                }
            }
        }

        return changes;
    }

    char find_color(std::vector<std::string> floor, int parity, char not_color) {
        std::map<char, int> freqs;
        int n = floor.size();

        for (char i = 'a'; i <= 'z'; ++i) {
            freqs[i] = 0;
        }

        for (int i = 0; i < n; ++i) {
            int row_parity = i % 2 == 0 ? parity : 1 - parity;
            for (int j = 0; j < n; ++j) {
                if (j % 2 == row_parity) {
                    char color = floor[i][j];
                    ++freqs[color];
                }
            }
        }

        char max_color = 0;
        int max_count = 0;

        for (auto it : freqs) {
            if (it.second > max_count and it.first != not_color) {
                max_count = it.second;
                max_color = it.first;
            }
        }

        return max_color;
    }
};
