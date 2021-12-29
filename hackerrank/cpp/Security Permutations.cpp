#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    cin >> n;
    
    vector<int> numbers(n, 0);
    
    for (int i = 0; i < n; ++i) {
        cin >> numbers[i];
    }
    
    for (int i = 0; i < n; ++i) {
        cout << numbers[numbers[i] - 1] << endl;
    }
    
    
    return 0;
}
