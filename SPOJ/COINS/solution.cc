#include <iostream>
#include <algorithm>
#include <map>

std::map<int, long long> memory;

long long f(int x) {
    if (x >= 0 and x <= 3) {
        return x;
    }
    if (memory.count(x) == 1) {
        return memory[x];
    }

    memory[x] = std::max((long long)x, f(x/2) + f(x/3) + f(x/4));
    return memory[x];
}

int main(void) {
    int n;

    while (std::cin >> n) {
        std::cout << f(n) << std::endl;
    }

    return 0;
}
