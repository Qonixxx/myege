#include <iostream>

int f(int n) {
	if (n == 1) return 1;
	if (n == 2) return 4;
	if (n > 2) return f(n - 1) * n + f(n - 2);
}

int main() {
	std::cout << f(7);
  	return 0;
}
