#include <iostream>

int f(int n) {
    if (n < 3) return 1;
    if (n > 2) return f((n + 1) / 2) + 1;
}

int main() {
    std::cout << f(2025); // ans - 11
    return 0;
}
