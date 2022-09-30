#include <iostream>

using namespace std;

int cnt[27];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	fill(cnt, cnt + 27, -1);
	string str;
	cin >> str;
	int index = 0;
	for (char c : str) {
		if (cnt[c - 'a'] == -1) {
			cnt[c - 'a'] = index;
		}
		index++;
	}
	for (int i = 0; i < 26; i++) {
		cout << cnt[i] << " ";
	}


}