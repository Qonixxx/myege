// given a array of nums and target num, 
// detect pair, suitable for the condition (a + b) == target
// example:
// [2, 41, 1, 4, 6, 0]
// target = 8;
// output: true

#include <bits/stdc++.h>
using namespace std;

// brute force approach
bool brute(vector <int> nums, int target) {
	for (int i = 0; i != nums.size(); i++) { // take one
		for (int j = i + 1; j != nums.size(); j++) { // take others 
			if (nums[i] + nums[j] == target) { 
				return true; // if sum equal target
			}
		}
	}
	// if searches are failed
	return false;
}

// two pointers
bool twoPointers(vector <int> arr, int target) {
	sort(begin(arr), end(arr));
	int left = 0, right = arr.size() - 1;
	while (left <= right) {
		int sum = arr[left] + arr[right];
		if (sum == target) {
			return true;
		}
		else if (sum < target) {
			left++;
		}
		else {
			right--;
		}
	}
	return false;
}

// program implementation
int main() {
	fast_cin();
	vector <int> nums = { 21, 2, 5, 9, 1, 6, 0 };
	int target = 100;
	// if (brute)
	if (twoPointers(nums, target)) {
		cout << "Pair are actually found!" << ln;
	}
	else {
		cout << "Target is not reached." << ln;
	}
	return 0;
}
