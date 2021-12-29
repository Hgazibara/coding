#include <bits/stdc++.h>

using namespace std;

// Complete the countingValleys function below.
int countingValleys(int n, string s) {
    vector<int> positions(n, 0);
    positions[0] = s[0] == 'U' ? 1 : -1;

    for (int i = 1; i < n; i++) {
        if (s[i] == 'U') {
            positions[i] = positions[i - 1] + 1;
        } else {
            positions[i] = positions[i - 1] - 1;
        }
    }

    int valleys = 0;
    int last_position = 0;

    for (int i = 0; i < n; i++) {
        if (positions[i] < 0 && last_position != -1) {
            valleys++;
            last_position = -1;
        } else if (positions[i] >= 0) {
            last_position = 1;
        }
    }

    return valleys;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string s;
    getline(cin, s);

    int result = countingValleys(n, s);

    fout << result << "\n";

    fout.close();

    return 0;
}
