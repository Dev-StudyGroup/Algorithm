#include <iostream>

using namespace std;

int num[9];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int flag = 0;
	for (int i = 0; i < 8; i++) {
		int cur_flag = 0;
		cin >> num[i];
		if (i == 0) {
			continue;
		}
		else {
			if (num[i] > num[i - 1]) cur_flag = 1;
			else if (num[i] < num[i - 1]) cur_flag = 2;
		}

		if (flag == 0) flag = cur_flag;
		else {
			if (flag != cur_flag) {
				flag = 3;
				break;
			}
		}
	}
	if (flag == 1) cout << "ascending";
	else if (flag == 2) cout << "descending";
	else cout << "mixed";
}