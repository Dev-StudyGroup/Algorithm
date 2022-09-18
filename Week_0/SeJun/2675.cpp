#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	cin >> n;
	while (n--) {
		int r;
		string str;
		cin >> r >> str;
		for (char c : str) {
			for (int i = 0; i < r; i++) {
				cout << c;
			}
		}
		cout << "\n";
	}

}