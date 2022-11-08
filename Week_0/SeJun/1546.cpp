#include <iostream>

using namespace std;

int num[1001];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cout << fixed;
	cout.precision(3);
	
	int n;
	int max = 0;
	double sum = 0.0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> num[i];
		if (num[i] > max) max = num[i];
	}

	for (int i = 0; i < n; i++) sum += (double)num[i] / max * 100.0;
	cout << sum / n;

}