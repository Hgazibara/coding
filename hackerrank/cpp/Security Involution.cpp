#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    cin >> n;
    
    vector<int> f1(n, 0);
    vector<int> f2(n, 0);
    
    for (int i = 0; i < n; ++i) {
        cin >> f1[i];
    }
    
    for (int i = 0; i < n; ++i) {
        f2[i] = f1[f1[i] - 1];
    }
    
    for (int i = 0; i < n; ++i) {
        if (f2[i] != i + 1) {
            cout << "NO";
            return 0;
        }
    }
    
    cout << "YES";
    
    return 0;
}
