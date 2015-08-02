#include <iostream>

int count_cards(double c);
double overhang(int n);

int main(void) {
    double c;
    std::cin >> c;

    while (c > 0) {
        std::cout << count_cards(c) << " card(s)" << std::endl;
        std::cin >> c;
    }

    return 0;
}

int count_cards(double c) {
    for (int n = 1; n <= 300; n++) {
        if (overhang(n) >= c) {
            return n;
        }
    }
    return -1;
}

double overhang(int n) {
    double overhang = 0.0;

    for (int i = n + 1; i >= 2; i--) {
        overhang += 1.0/i;
    }

    return overhang;
}
