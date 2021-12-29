#include <cmath>
#include <climits>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int N, K, P;
    int min, tmp, iter;
    vector<int> packets;
    vector<int> diffs;
    
    cin >> N;
    cin >> K;
    iter = 0;
    
    while(iter < N) {
        cin >> P;
        packets.push_back(P);
        ++iter;
    }
    
    sort(packets.begin(), packets.end());
    min = INT_MAX;
    
    for(int i = 0, limit = N - K; i <= limit; ++i) {
        for(int j = i + K - 1; j < N; ++j) {
            tmp = packets[j] - packets[i];
            if(tmp > min && j > (i + K - 1)) {
                break;
            }
            if(tmp < min) {
                min = tmp;
            }
        }
    }
    
    cout << min;
    
    return 0;
}