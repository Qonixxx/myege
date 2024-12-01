// такой код писать не рекомендуется, можно разобрать, но не повторять, так как тут очень много лишнего
// оставляю его тут, т.к хочу оставить свой труд (было оч много отладки и дебага, прежде чем я получил правильный ответ)


/*
 В файле содержится последовательность целых чисел. 
 Элементы последовательности могут принимать значения от 0 до 200 включительно. 
 Определите сначала количество троек элементов последовательности, 
 в которых хотя бы одно число в троичной системе счисления оканчивается 2, 
 а затем сумму минимальных чисел из таких троек. 
 Под тройкой подразумевается три идущих подряд элемента последовательности.
*/

#include <iostream> // std::cout
#include <vector> // std::vector  
#include <fstream> // std::ifstream
#include <string> // std::string; std::stoi
#include <numeric> // std::accumulate
#include <algorithm> // std::reverse

std::string toBase(std::string x, int base) {
    std::string res = "";
    int n = std::stoi(x);
    while (n) {
        res += std::to_string(n % base);
        n /= base;
    }
    std::reverse(res.begin(), res.end());
    return res;
}

int comp(int a, int b, int c) {
    // знак <= обязателен
    if ((a <= b) && (a <= c)) return a;
    else if ((b <= a) && (b <= c)) return b;
    else if ((c <= a) && (c <= b)) return c;
    return 0; // опционально для компилятора, данная строчка не имеет никакого значения
}

int lastLetter(std::string s) {
    char x = s[s.size() - 1];
    if (x == '2') return 1;
    else return 0;
}

int main() {
    std::ifstream f("17.txt");
    std::vector <std::string> a;
    std::vector <int> ans; 
    std::string x;
    while (f >> x) {
        a.push_back(x);
    }
//    std::cout << lastLetter(toBase(a[140], 3));
    
    for (int i = 0; i != a.size() - 2; i++) {
        if (lastLetter(toBase(a[i], 3)) == 1  || lastLetter(toBase(a[i + 1], 3)) == 1 || lastLetter(toBase(a[i + 2], 3)) == 1) {
            ans.push_back(comp(std::stoi(a[i]), std::stoi(a[i + 1]), std::stoi(a[i + 2])));
        }
    }
//    for (int i = 0; i != ans.size(); i++) {
//        std::cout << ans[i] << " ";
//    }
    std::cout << ans.size() << " " << std::accumulate(ans.begin(), ans.end(), 0); // 91 2627
    
}
