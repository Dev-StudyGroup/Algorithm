#include <iostream>

using namespace std;

int num[6];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int sum = 0;
	
	for (int i = 0; i < 5; i++) {
		cin >> num[i];
	}

	for (int i = 0; i < 5; i++) {
		sum += (num[i] * num[i]) % 10;
		sum = sum % 10;
	}
	cout << sum;
}