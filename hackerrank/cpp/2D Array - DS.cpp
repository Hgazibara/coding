#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main(){
    vector< vector<int> > arr(6, vector<int>(6));
    for(int arr_i = 0; arr_i < 6; arr_i++){
       for(int arr_j = 0; arr_j < 6; arr_j++){
          cin >> arr[arr_i][arr_j];
       }
    }
    
    int maximum_sum = -1000;
    
    for (int arr_i = 0; arr_i < 4; arr_i++) {
        for (int arr_j = 0; arr_j < 4; arr_j++) {
            int current_sum = arr[arr_i][arr_j] + arr[arr_i][arr_j+1] + arr[arr_i][arr_j+2] + arr[arr_i+1][arr_j+1] + arr[arr_i+2][arr_j] + arr[arr_i+2][arr_j+1] + arr[arr_i+2][arr_j+2];
            maximum_sum = max(maximum_sum, current_sum);
        }
    }
    
    cout << maximum_sum;
    
    return 0;
}
