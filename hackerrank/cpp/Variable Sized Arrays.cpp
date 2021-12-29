#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, q;
    cin >> n >> q;
    
    int** arrays = new int*[n];
    
    int i = 0;
    
    while (i < n) {
        int k;
        int j = 0;
        cin >> k;
        
        arrays[i] = new int[k];
        
        while (j < k) {
            cin >> arrays[i][j];
            ++j;
        }
        
        ++i;
    }
    
    int a, b;
    
    while (q-- > 0) {
        cin >> a >> b;
        cout << arrays[a][b] << endl;
    }
    
    return 0;
}
