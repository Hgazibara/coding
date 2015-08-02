#include <iostream>
#include <string>

bool is_palindrome(std::string s) {
    int n = s.size();

    for (int i = 0; i < n/2; ++i) {
        if (s[i] != s[n - i - 1]) {
            return false;
        }
    }

    return true;
}

int find(std::string s) {
    for (int i = 0; ; ++i) {
        std::string temp = std::string(s);
        for (int j = i - 1; j >= 0; --j) {
            temp += s[j];
        }
        if (is_palindrome(temp)) {
            return i + s.size();
        }
    }
}

int main(void) {
    std::string input;

    while (true) {
        std::cin >> input;
        if (input.size() > 0) {
            std::cout << find(input) << std::endl;
        } else {
            break;
        }
    }

    return 0;
}
