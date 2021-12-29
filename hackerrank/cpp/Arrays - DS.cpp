#include <string>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;


int main(){
    int n;
    cin >> n;
    
    vector<int> arr(n);
    for(int arr_i = 0; arr_i < n; arr_i++) {
       cin >> arr[arr_i];
    }
    
    for (int arr_i = n - 1; arr_i >= 0; arr_i--) {
        if (arr_i < n - 1) {
            cout << ' ';
        }
        cout << arr[arr_i];
    }
    return 0;
}
