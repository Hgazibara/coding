#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int n, q;
    int sum = 0;
    
    cin >> n;
    
    for(int arr_i = 0;arr_i < n;arr_i++){
       cin >> q;
       sum += q;
    }
    
    cout << sum;
    
    return 0;
}
