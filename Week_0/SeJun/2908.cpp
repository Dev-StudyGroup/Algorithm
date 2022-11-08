#include <iostream>
#include <string>
#include <algorithm> // reverse

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	string num1, num2;
	int rnum1, rnum2;
	cin >> num1 >> num2;
	reverse(num1.begin(), num1.end());
	reverse(num2.begin(), num2.end());
	rnum1 = stoi(num1);
	rnum2 = stoi(num2);
	if (rnum1 > rnum2) cout << rnum1;
	else cout << rnum2;
}