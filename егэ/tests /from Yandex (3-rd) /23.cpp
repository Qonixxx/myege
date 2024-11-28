#include <iostream>

int f(int s, int e) {
  if (s > e || s == 35) return 0;
  if (s == e) return 1;
  else return f(s + 1, e) + f(s + 2, e) + f(s + 4, e);
}

int main() {
  std::cout << f(24, 33) * f(33, 42);
}
