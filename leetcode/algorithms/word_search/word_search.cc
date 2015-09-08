int i_moves[] = {1, -1, 0, 0};
int j_moves[] = {0, 0, 1, -1};
char visited = '#';

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        if (word.size() == 0) {
            return false;
        }

        int rows = board.size();
        int cols = board[0].size();

        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (board[i][j] == word[0]) {
                    string target = word.substr(1);

                    char temp = board[i][j];
                    board[i][j] = visited;

                    bool can_find = this->find(board, i, j, target);

                    if (can_find) {
                        return true;
                    }

                    board[i][j] = temp;
                }
            }
        }

        return false;
    }

    bool find(vector<vector<char>>& board, int i, int j, string word) {
        if (word.size() == 0) {
            return true;
        }

        int m = board.size();
        int n = board[0].size();

        for (int k = 0; k < 4; ++k) {
            int ni = i + i_moves[k];
            int nj = j + j_moves[k];

            if (ni < 0 || ni == m || nj < 0 || nj == n || board[ni][nj] != word[0] || board[ni][nj] == visited) {
                continue;
            }

            char temp = board[ni][nj];
            board[ni][nj] = visited;

            bool can_find = this->find(board, ni, nj, word.substr(1));

            if (can_find) {
                return true;
            }

            board[ni][nj] = temp;
        }

        return false;
    }
};
