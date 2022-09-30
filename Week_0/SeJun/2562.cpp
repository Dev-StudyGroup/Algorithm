#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int num, index;
	int max = 0;
	for (int i = 0; i < 9; i++) {
		cin >> num;
		if (num > max) {
			max = num;
			index = i;
		}
	}
	cout << max << "\n";
	cout << index + 1;
}