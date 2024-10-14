// given a array of numbers and target
// task: find target in array (if target not found - print "Target isn't detected")
// example:
// arr = [7, 2, 6, 1, 2]
// target = 6
// ans: 6

#include <bits/stdc++.h>
using namespace std;

typedef vector <int> vi;

#define fast_cin() \
    ios_base::sync_with_stdio(0); \
    cin.tie(NULL); \
    cout.tie(NULL)
#define ln "\n"
#define all(x) begin(x), end(x)
#define sortall(x) sort(all(x))

// 1. Linear search (O(n))
void findTarget(vi arr, int target) {
    auto res(find(all(arr), target));
    if (res == end(arr)) {
        cout << "Target isn't detected." << ln;
    }
    else {
        cout << arr[res - begin(arr)] << ln;
    }
}

// 2. Binary search (O(log n)) 
void binS(vi arr, int target) {
    sortall(arr);
    int left = 0, right = arr.size() - 1;
    bool flag = false;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (arr[mid] == target) {
            cout << arr[mid] << ln;
            flag = true;
            break;
        }
        if (arr[mid] > target) {
            right = mid--;
        }
        else {
            left = mid++;
        }
    }
    if (flag == false) {
        cout << "Target isn't detected." << ln;
    }
}

int main() {
    // test case
    vi a = {66, 3, 2, 100, 300, 8, 310};
    int target = 300;
//  findTarget(a, target);
    binS(a, target);
    return 0;
}
