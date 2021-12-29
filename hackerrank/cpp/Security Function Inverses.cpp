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
    
    for(int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        numbers[a - 1] = i + 1;
    }
    
    for(int i = 0; i < n; ++i) {
        cout << numbers[i] << endl;
    }
    
    return 0;
}
