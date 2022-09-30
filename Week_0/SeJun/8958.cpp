#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	cin >> n;
	while (n--) {
		string str;
		cin >> str;
		int cnt = 1;
		int sum = 0;
		for (char c : str) {
			if (c == 'O') {
				sum += cnt;
				cnt++;
			}
			else {
				cnt = 1;
			}
		}
		cout << sum << "\n";
	}

}