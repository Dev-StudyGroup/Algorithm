#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		for (int j = 0; j < n - i; j++) {
			cout << " ";
		}
		for (int j = n - i; j < n; j++) {
			cout << "*";
		}
		cout << "\n";
	}

}