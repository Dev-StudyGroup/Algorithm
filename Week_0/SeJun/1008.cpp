#include <iostream>
#include <iomanip> // ���е� ����

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int a, b;
	double result;
	cin >> a >> b;
	result = (double)a / (double)b;
	//  cout << fixed; (�Ҽ��� ���Ϸ� ����)
	cout.precision(12); // �Ҽ��� 12�� ����
	cout << result;

}