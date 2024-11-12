// https://inf-ege.sdamgia.ru/problem?id=27423

#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream f("26.txt");
    int s, n;
    f >> s >> n;
    int x;
    vector <int> a;
    while (f >> x) {
        a.push_back(x);
    }
    sort(a.begin(), a.end());
    int sum = 0;
    int k = 0;
    int maxi = 0;
    for (int i = 0; i != a.size(); i++) {
        if (a[i] + sum <= s) {
        sum += a[i];
        maxi = i + 1;
        }
    }
    int t = a[maxi];
    for (int i = maxi + 1; i != a.size(); i++) {
        if ((sum - t + a[i]) <= s) {
            sum = sum - t + a[i];
            t = a[i];
        }
    }
    cout << maxi << " " << t << "\n";
    return 0;
}
