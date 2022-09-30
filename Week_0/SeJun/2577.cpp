#include <iostream>
#include <string>

using namespace std;

int num[11];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int a, b, c;
	int result;
	string str;
	cin >> a >> b >> c;
	result = a * b * c;
	str = to_string(result);
	for (char c : str) num[c - '0']++;
	for (int i = 0; i < 10; i++) cout << num[i] << "\n";

}