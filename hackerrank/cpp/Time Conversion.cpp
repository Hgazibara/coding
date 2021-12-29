#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    string time;
    cin >> time;
    
    int hours = atoi(time.substr(0, 2).c_str());
    string type = time.substr(8, 2);
    
    if (type == "PM" && hours < 12 ) {
        hours += 12;
    } else if (type == "AM" && hours == 12) {
        hours = 0;
    }
    
    printf("%02d%s", hours, time.substr(2, 6).c_str());
    
    return 0;
}
