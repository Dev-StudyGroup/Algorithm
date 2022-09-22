#include <iostream>
#include <string>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	string str;
	int cnt = 0, cur = 0;
	getline(cin, str);
	for (char c : str) {
		if (c == ' ') {
			cnt++;
		}

		cur++;

		if (cur == 1 && c == ' ') {
			cnt--;
		}

		if (cur == str.length() && c != ' ') {
			cnt++;
		} 
	}
	cout << cnt;

}