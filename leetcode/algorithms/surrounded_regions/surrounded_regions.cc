int x_moves[] = {1, -1, 0, 0};
int y_moves[] = {0, 0, 1, -1};

class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int rows = board.size();

        if (rows == 0) {
            return;
        }

        int cols = board[0].size();

        vector<vector<bool>> doesNotLeak(rows, vector<bool>(cols, true));
        this->findLeakagePoints(board, doesNotLeak);

        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (board[i][j] == 'O' && doesNotLeak[i][j]) {
                    board[i][j] = 'X';
                }
            }
        }
    }

    void findLeakagePoints(vector<vector<char>>& board, vector<vector<bool>>& doesNotLeak) {
        int X = board.size() - 1;
        int Y = board[0].size() - 1;

        queue<pair<int, int>> q;

        for (auto &point: this->getOuterPoints(board)) {
            if (board[point.first][point.second] == 'X') {
                continue;
            }
            q.push(point);
        }

        while (!q.empty()) {
            pair<int, int> top = q.front();
            q.pop();

            int x = top.first;
            int y = top.second;

            if (x == 0 || x == X || y == 0 || y == Y) {
                doesNotLeak[x][y] = false;
            }

            for (auto &next: this->getNeighbors(board, x, y)) {
                if (doesNotLeak[next.first][next.second] == false) {
                    continue;
                }

                if (doesNotLeak[x][y] == false) {
                    doesNotLeak[next.first][next.second] = false;
                }

                q.push(next);
            }
        }
    }

    vector<pair<int, int>> getOuterPoints(vector<vector<char>>& board) {
        int rows = board.size();
        int cols = board[0].size();

        vector<pair<int, int>> outerPoints;

        for (int i = 0; i < rows; ++i) {
            outerPoints.push_back(make_pair(i, 0));
            outerPoints.push_back(make_pair(i, cols - 1));
        }

        for (int j = 0; j < cols; ++j) {
            outerPoints.push_back(make_pair(0, j));
            outerPoints.push_back(make_pair(rows - 1, j));
        }

        return outerPoints;
    }

    vector<pair<int, int>> getNeighbors(vector<vector<char>>& board, int x, int y) {
        int X = board.size() - 1;
        int Y = board[0].size() - 1;

        vector<pair<int, int>> neighbors;

        for (int i = 0; i < 4; ++i) {
            int nx = x + x_moves[i];
            int ny = y + y_moves[i];

            if (nx < 0 || nx > X || ny < 0 || ny > Y || board[nx][ny] == 'X') {
                continue;
            }

            neighbors.push_back(make_pair(nx, ny));
        }

        return neighbors;
    }
};
