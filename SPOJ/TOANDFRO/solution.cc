#include <iostream>
#include <algorithm>
#include <string>

std::vector<std::string> to_grid(std::string message, int columns) {
    std::vector<std::string> grid;
    int rows = message.size() / columns;
    int position = 0;

    for (int row = 0; row < rows; row++) {
        std::string column;
        for (int col = 0; col < columns; ++col) {
            column.push_back(message[position++]);
        }
        if (row % 2 == 1) {
            std::reverse(column.begin(), column.end());
        }
        grid.push_back(column);
    }

    return grid;
}

std::string decode(std::string& message, int columns) {
    std::vector<std::string> grid = to_grid(message, columns);
    std::string output;

    int rows = message.size() / columns;
    int position = 0;

    for (int col = 0; col < columns; ++col) {
        for (int row = 0; row < rows; row++) {
            output.push_back(grid[row][col]);
        }
    }

    return output;
}

int main(void) {
    int columns;
    std::cin >> columns;

    while (columns != 0) {
        std::string message;
        std::cin >> message;

        std::cout << decode(message, columns) << std::endl;

        std::cin >> columns;
    }

    return 0;
}
