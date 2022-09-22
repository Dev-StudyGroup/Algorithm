#include <iostream>

using namespace std;

int cnt[43];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int num;
	int result = 0;
	for (int i = 0; i < 10; i++) {
		cin >> num;
		cnt[num % 42]++;
	}
	for (int i = 0; i < 42; i++) {
		if (cnt[i] > 0) result++;
	}
	cout << result;
}