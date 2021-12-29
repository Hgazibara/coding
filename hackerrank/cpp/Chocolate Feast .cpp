#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int T;
    cin >> T;
    
    while(T > 0) {
        
        int N, C, M;
        int papers, eaten;
        
        cin >> N >> C >> M;
        papers = eaten = N/C;
        
        while(papers >= M) {
            papers += 1 - M;
            eaten += 1;
        }
        
        cout << eaten << endl;
        
        --T;
    }
    return 0;
}
