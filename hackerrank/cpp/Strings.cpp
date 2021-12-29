#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a, b;

    cin >> a;
    cin >> b;

    string c = a + b;
    string d = a + " " + b;

    d[0] = b[0];
    d[a.size() + 1] = a[0];

    cout << a.size() << ' ' << b.size() << endl;
    cout << c << endl;
    cout << d << endl;


    return 0;
}

