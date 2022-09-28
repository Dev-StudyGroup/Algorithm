#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n, num;
	int min, max;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> num;
		if(i == 0) {
			min = num;
			max = num;
			continue;
		}

		if (min > num) min = num;
		if (max < num) max = num;
	}
	cout << min << " " << max;

}