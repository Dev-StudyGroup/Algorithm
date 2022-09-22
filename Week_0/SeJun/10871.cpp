#include <iostream>
#include <vector>


using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	vector<int> v;

	int n, x;
	int num;
	cin >> n >> x;
	for (int i = 0; i < n; i++) {
		cin >> num;
		if (num < x) v.push_back(num);
	}
	for (auto it = v.begin(); it < v.end(); it++) cout << *it << " ";

}