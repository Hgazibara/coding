#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0;arr_i < n;arr_i++){
       cin >> arr[arr_i];
    }
    
    long long int sum = 0;
    
    for (auto it = arr.begin(); it != arr.end(); ++it) {
        sum += *it;
    }
    
    cout << sum;
    
    return 0;
}
