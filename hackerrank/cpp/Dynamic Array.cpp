#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define INDEX(a, b, c) (((a)^(b))%(c))

int main() {
    int n, q;
    cin >> n >> q;

    int last_answer = 0;
    vector<vector<int>> sequences(n, vector<int>(0));
    
    for (int i = 0; i < q; i++) {
        int t, x, y;
        cin >> t >> x >> y;
        
        if (t == 1) {
            sequences[INDEX(x, last_answer, n)].push_back(y);
        } else if (t == 2) {
            int index = INDEX(x, last_answer, n);
            vector<int> seq = sequences[index];
            last_answer = seq[y % seq.size()];
            cout << last_answer << '\n';
        }
    }

    return 0;
}
