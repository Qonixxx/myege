#include <bits/stdc++.h>
using namespace std;

int main() {
    for (int a = 1; a <= 1000; a++) {
        bool flag = true;
        for (int x = 1; x <= 1000; x++) {
            if ( ( (((x % 3) == 0) <= ((x % 4) != 0)) or ( (x + a) >= 138) ) == 0) {
                flag = false;
                break;
            }
        }
        if (flag) {
		cout << a << endl;
		break; 
    	}	
	  }
}
