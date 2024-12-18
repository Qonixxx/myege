#include <iostream>

int f(int s, int e) {
  if (s > e || s == 17) return 0;
  if (s == e) return 1;
  else return f(s + 2, e) + f(s + 3, e) + f(s * 2, e);
}

int main() {
  std::cout << f(3, 10) * f(10, 25);
}
