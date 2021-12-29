#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int N;
	
    string pattern("hackerrank");
    string s;
	
    cin >> N;
	getline(cin, s);
	
    for(int i = 0; i < N; ++i) {
        getline(cin, s);
		
		int first = s.find(pattern.c_str());
		int last = s.rfind(pattern.c_str());
		int diff = s.size()-pattern.size();
		
		if((first == 0 && last == 0 && s.size()==pattern.size()) || (first == 0 && last == diff)) {
			cout << 0;
		} else if((first == 0 && last == 0 && s.size() != pattern.size()) || (first == 0 && last > 0 && last < diff)) {
			cout << 1;
		} else if(first != 0 && last == diff) {
			cout << 2;
		} else {
			cout << -1;
		}
		
		cout << endl;
    }
	
    return 0;
}