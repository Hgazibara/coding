#include <iostream>
#include <string>
#include <map>

void init_counters(std::map<std::string, int>& counters);
void count_sequences(std::string input, std::map<std::string, int>& counters);
void print_counters(int N, std::map<std::string, int>& counters);

const std::string sequences[] = {
    "TTT", "TTH", "THT", "THH", "HTT", "HTH", "HHT", "HHH"
};

int main(void) {
    int T;
    std::cin >> T;

    while (T > 0) {
        int N;
        std::string input;
        std::map<std::string, int> counters;
        init_counters(counters);

        std::cin >> N;
        std::cin >> input;

        count_sequences(input, counters);
        print_counters(N, counters);

        T--;
    }

    return 0;
}

void init_counters(std::map<std::string, int>& counters) {
    for (int i = 0; i < 8; i++) {
        counters[sequences[i]] = 0;
    }
}

void count_sequences(std::string input, std::map<std::string, int>& counters) {
    int end = input.size() - 2;

    for (int start = 0; start < end; start++) {
        counters[input.substr(start, 3)] += 1;
    }
}

void print_counters(int N, std::map<std::string, int>& counters) {
    std::cout << N;

    for (int i = 0; i < 8; i++) {
        std::cout << " " << counters[sequences[i]];
    }

    std::cout << std::endl;
}
