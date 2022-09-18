#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int h, m;

	cin >> h >> m;

	if (m < 45) {
		h -= 1;
		h = (24 + h) % 24;
		m -= 45;
		m = (60 + m) % 60;
	}
	else {
		m -= 45;
	}

	cout << h << " " << m;

}