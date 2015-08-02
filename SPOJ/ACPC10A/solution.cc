#include <iostream>

int main(void) {
    int A, B, C;
    std::cin >> A >> B >> C;

    while (!(A == 0 && B == 0 && C == 0))  {
        if ((B - A == C - B) && (A != B)) {
            std::cout << "AP " <<  C + C - B << std::endl;
        } else {
            std::cout << "GP " << C * C / B << std::endl;
        }
        std::cin >> A >> B >> C;
    }

    return 0;
}
