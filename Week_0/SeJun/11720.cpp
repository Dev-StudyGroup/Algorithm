#include <iostream>


using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n;
	char num;
	int sum = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> num;
		sum += (num - '0');
	}
	cout << sum;

}