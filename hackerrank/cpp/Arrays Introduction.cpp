#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void read_and_display(int level) {
    if (level == 0) {
        return;
    }
    int a;
    cin >> a;
    read_and_display(level - 1);
    cout << a << ' ';
}

int main() {
    int n;
    cin >> n;
    
    read_and_display(n); 
    
    return 0;
}
