// сортировка "пузырьком" - основа всего решения

#include <bits/stdc++.h>
using namespace std;

int main() {
	ifstream f("demo_2025_26.txt");
	int n;
	f >> n;
	vector <vector <double>> all;
	vector <vector <double>> gods;
	vector <vector <double>> bad;
	int count = 0;
	for (int i = 0; i != n; i++) {
		double id, m1, m2, m3, m4;
		f >> id >> m1 >> m2 >> m3 >> m4;
		all.push_back({ id, m1, m2, m3, m4 });
	}
	for (int i = 0; i != n; i++) {
		bool change = true;
		for (int j = 0; j != 5; j++) {
			if (all[i][j] == 2) {
				bad.push_back(all[i]);
				change = false;
				break;
			}
		}
		if (change) {
			gods.push_back(all[i]);
		}
	} // в этом блоке кода мы распределяем студентов на группы (сдавшие / не сдавшие сессию)
	vector <vector <double>> gods_average;
	vector <vector <double>> bad_average;
	for (int i = 0; i != gods.size(); i++) {
		double sum = 0;
		double average = 0;
		for (int j = 1; j != 5; j++) {
			sum += gods[i][j];
		}
		average = sum / 4.0;
		gods_average.push_back({ gods[i][0], average });
	}
	for (int i = 0; i != bad.size(); i++) {
		int sum = 0;
		double average = 0;
		double twoCount = 0;
		for (int j = 1; j != 5; j++) {
			sum += bad[i][j];
			if (bad[i][j] == 2) {
				twoCount++;
			}
		}
		average = sum / 4.0;
		bad_average.push_back({ bad[i][0], average, twoCount });
	} // здесь мы выясняем средний балл у всех студентов, а у не сдавших вдобавок кол-во двоек
	for (int i = 0; i != gods_average.size() - 1; i++) {
		for (int j = 0; j != gods_average.size() - 1 - i; j++) {
			if (gods_average[j + 1][1] > gods_average[j][1]) {
				swap(gods_average[j], gods_average[j + 1]);
			}
			else if (gods_average[j + 1][1] == gods_average[j][1]) {
				if (gods_average[j + 1][0] < gods_average[j][0]) {
					swap(gods_average[j + 1], gods_average[j]);
				}
			} // реализация сортировки
		}
	}
	for (int i = 0; i != bad_average.size() - 1; i++) {
		for (int j = 0; j != bad_average.size() - 1 - i; j++) {
			if (bad_average[j + 1][2] < bad_average[j][2]) {
				swap(bad_average[j + 1], bad_average[j]);
			}
			else if (bad_average[j + 1][2] == bad_average[j][2]) {
				if (bad_average[j + 1][1] > bad_average[j][1]) {
					swap(bad_average[j + 1], bad_average[j]);
				}
				else if (bad_average[j + 1][1] == bad_average[j][1]) {
					if (bad_average[j + 1][0] < bad_average[j][0]) {
						swap(bad_average[j + 1], bad_average[j]);
					}
				}
			}
		}
	}
	
	// вывод людей со степендией
	for (int i = 0; i != 2491; i++) { // 2491 - первые 25% рейтинга (расчитано в калькуляторе)
		for (int j = 0; j != 2; j++) {
			cout << gods_average[i][j] << " ";
		}
		cout << endl;
	}

	// ответ - 52325
	

	// вывод людей без степендии
	for (int i = 0; i != bad_average.size(); i++) {
		for (int j = 0; j != 3; j++) {
			cout << bad_average[i][j] << " ";
		}
		cout << "\n";
	}
	// ответ - 635
	return 0;
