#include <vector>
#include <cstdio>
#include <iostream>

using namespace std;


int main(){
    int n;
    cin >> n;
    
    int max_height = 0;
    
    vector<int> height(n);
    for(int height_i = 0; height_i < n; height_i++){
        cin >> height[height_i];
        max_height = height[height_i] > max_height ? height[height_i] : max_height;
    }
    
    int total_candles = 0;
    
    for(int height_i = 0; height_i < n; height_i++){
        if (height[height_i] == max_height) {
            ++total_candles;
        }
    }
    
    cout << total_candles;
    
    return 0;
}
