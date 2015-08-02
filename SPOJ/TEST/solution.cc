#include <iostream>

int main(void) {

    int in;

    while (true) {
        std::cin >> in;
        
        if (in == 42) {
            break;
        }

        std::cout << in << std::endl;
    }

    return 0;
}
