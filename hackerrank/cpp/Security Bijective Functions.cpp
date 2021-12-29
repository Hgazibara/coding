#include <cmath>
#include <cstdio>
#include <set>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, a;
    int sum = 0;
    
    cin >> n;
    
    int i = 0;
    
    while (i++ < n) {
        cin >> a;
        sum += a;
    }
    
    cout << (sum == n * (n + 1) / 2 ? "YES" : "NO");
    
    return 0;
}
