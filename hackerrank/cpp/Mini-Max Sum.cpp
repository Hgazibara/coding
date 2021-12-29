#include <bits/stdc++.h>

using namespace std;

int main() {
    vector<int> arr(5);
    long long int total_sum = 0;
    
    int min_arr = 1000000000;
    int max_arr = 0;
    
    for(int arr_i = 0; arr_i < 5; arr_i++){
       cin >> arr[arr_i];
        total_sum += arr[arr_i];
        min_arr = arr[arr_i] < min_arr ? arr[arr_i] : min_arr;
        max_arr = arr[arr_i] > max_arr ? arr[arr_i] : max_arr;
    }
    
    cout << (total_sum - max_arr) << ' ' << (total_sum - min_arr) << endl;
    
    return 0;
}
