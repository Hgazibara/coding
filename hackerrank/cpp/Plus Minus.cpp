#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int n, current;
    cin >> n;
    
    int positives, negatives, zeros;
    positives = negatives = zeros = 0;
    
    int i = 0;
    
    while (i++ < n) {
        cin >> current;
        if (current > 0) {
            ++positives;
        } else if (current < 0) {
            ++negatives;
        } else {
            ++zeros;
        }
    }
    
    printf("%.6f\n", (float)positives / n);
    printf("%.6f\n", (float)negatives / n);
    printf("%.6f\n", (float)zeros / n);
    
    return 0;
}
