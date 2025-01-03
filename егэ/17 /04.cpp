/*
В файле содержится последовательность целых чисел. 
Элементы последовательности могут принимать целые значения от –10 000 до 10 000 включительно. 
Определите и запишите в ответе сначала количество троек элементов последовательности, 
в которых хотя бы одно число кратно 12, а каждое число делится на 3, 
затем минимальное из средних арифметических элементов таких троек. 
В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream f("17.txt");
    vector <int> a;
    int x;
    while (f >> x) {
        a.push_back(x);
    }
    vector <int> ans;
    for (int i = 0; i != a.size() - 2; i++) {
        if ( ((a[i] % 12 ) == 0) || ((a[i + 1]) % 12 == 0) || ((a[i + 2] % 12) == 0 )) {
            if ( ((a[i] % 3) == 0) && ((a[i + 1] % 3) == 0) && ((a[i + 2] % 3) == 0) ) {
                ans.push_back( ( a[i] + a[i + 1] + a[i + 2] ) / 3);
            }
        }
    }
    cout << ans.size() << " " << *min_element(begin(ans), end(ans));
    return 0;
}
