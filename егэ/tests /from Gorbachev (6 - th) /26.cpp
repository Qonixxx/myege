#include <bits/stdc++.h>
using namespace std;

#define fast_cin() \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL); \
    cout.tie(NULL)

int main() {
    fast_cin();
    ifstream f("26.txt");
    int n; f >> n;
    vector <int> all(24 * 60);
    for (int i = 0; i != n; i++) {
        int in, out; f >> in >> out; 
        all[in]++; all[out]--;
    }
    int cnt = 0;
    int mx = -1000000;
    for (int i = 0; i != 1440; i++) {
        cnt += all[i];
        mx = max(mx, cnt);
    }
    cnt = 0;
    int k = 0;
    for (int i = 0; i != 1440; i++) {
        cnt += all[i];
        if (cnt == mx && all[i] != 0) {
            k++;
        }
    }
//    for (int i = 0; i != all.size(); i++) {
//        cout << all[i] << " ";
//    }
    cout << k << " " << mx << "\n";
    return 0;
}
