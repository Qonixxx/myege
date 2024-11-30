/*
В файле содержится последовательность целых чисел.
Элементы последовательности могут принимать целые значения от –10 000 до 10 000 включительно. 
Определите и запишите в ответе сначала количество пар элементов последовательности, 
сумма которых кратна 3 и не кратна 6, а произведение оканчивается на 8,
затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
*/

#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
#include <cmath>
using namespace std;

typedef vector <int> vi;
#define fast_cin() \
  ios_base::sync_with_stdio(false); \
  cin.tie(NULL); \
  cout.tie(NULL);


int main() {
  fast_cin();
  ifstream f("17.txt");
  vi a;
  int x;
  int cnt = 0;
  while (f >> x) {
    a.push_back(x);
  }
  int mx = -100000;
  for (int i = 0; i != a.size() - 1; i++) {
    if (((a[i] + a[i + 1]) % 3 == 0 && (a[i] + a[i + 1]) % 6 != 0) && (abs(a[i] * a[i + 1]) % 10 == 8)) {
      mx = max(mx, a[i] + a[i + 1]);
      cnt++;
    }
  }
  cout << cnt << " " << mx; // 140 17031
}
