#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n, flag = 0;

	cin >> n;
	if (n % 4 == 0) flag = 1;
	if (n % 100 == 0) flag = 0;
	if (n % 400 == 0) flag = 1;
	cout << flag;

}