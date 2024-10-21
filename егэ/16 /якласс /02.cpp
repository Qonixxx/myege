#include <iostream>

int f(int n) {
	if (n == 1) return 2;
	if (n > 1 && n % 2 == 0) return 2 * n + f(n - 3);
	if (n > 1 && !(n % 2 == 0)) return 2 * (f(n + 1));
}

int main() {
	std::cout << f(13); // ans - 1592
	return 0;
}
