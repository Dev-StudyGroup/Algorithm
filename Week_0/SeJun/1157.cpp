#include <iostream>

using namespace std;

int word[27];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	string str;
	int max = -1;
	int max_num;
	int max_cnt = 0;
	cin >> str;
	for (char c : str) {
		if (c >= 65 && c <= 90) {
			word[c - 65]++;
		}
		else if (c >= 97 && c <= 122) {
			word[c - 97]++;
		}
	}

	for (int i = 0; i < 26; i++) {
		if(word[i] > max) {
			max = word[i];
			max_num = i;
			max_cnt = 1;
		}
		else if (word[i] == max) {
			max_cnt++;
		}
	}

	if (max_cnt > 1) cout << "?";
	else {
		char result(max_num + 65);
		cout << result;
	}

}