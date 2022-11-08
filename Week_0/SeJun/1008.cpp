#include <iostream>
#include <iomanip> // 정밀도 정의

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int a, b;
	double result;
	cin >> a >> b;
	result = (double)a / (double)b;
	//  cout << fixed; (소숫점 이하로 고정)
	cout.precision(12); // 소숫점 12개 까지
	cout << result;

}