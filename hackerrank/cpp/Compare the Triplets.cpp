#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> alice(3, 0);
    vector<int> bob(3, 0);

    cin >> alice[0] >> alice[1] >> alice[2];
    cin >> bob[0] >> bob[1] >> bob[2];
    
    int points_alice = 0;
    int points_bob = 0;
    
    for (int i = 0; i < 3; ++i) {
        if (alice[i] > bob[i]) {
            ++points_alice;
        } else if (alice[i] < bob[i]) {
            ++points_bob;
        }
    }
    
    cout << points_alice << ' ' << points_bob << endl;
    
    return 0;
}
