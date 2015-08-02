#include <string>

class BearCheats {
public:
	std::string eyesight(int A, int B) {
		int different = 0;

		while (A != 0) {
			int a_digit = A % 10;
			int b_digit = B % 10;

			if (a_digit != b_digit) {
				++different;
			}

			A = A / 10;
			B = B/10;
		}

		return different <= 1 ? "happy" : "glasses";
	}
};
