#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int a, b;
	cin >> a >> b;
	if (a > b) cout << ">";
	else if (a < b) cout << "<";
	else cout << "==";
}