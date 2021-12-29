#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int n;
    cin >> n;
    
    int sum_i, sum_j;
    vector< vector<int> > a(n,vector<int>(n));
    
    for(int a_i = 0;a_i < n;a_i++){
       for(int a_j = 0;a_j < n;a_j++){
          cin >> a[a_i][a_j];
       }
    }
    
    for (int i = 0; i < n; ++i) {
        sum_i += a[i][i];
        sum_j += a[i][n - i - 1];
    }
    
    cout << (sum_i > sum_j ? sum_i - sum_j : sum_j - sum_i);
    
    return 0;
}
