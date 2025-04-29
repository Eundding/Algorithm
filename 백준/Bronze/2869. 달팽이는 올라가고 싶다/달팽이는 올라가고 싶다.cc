 //2869번 달팽이는 올라가고 싶다
#include <iostream>
using namespace std;
int height(int a, int b, int v) {
	int height{ 0 }, day{ 0 };
	day = (v - b - 1) / (a - b) + 1;
	return day;
}
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int A, B, V, h(0);
	cin >> A >> B >> V;
	
	cout << height(A, B, V);
}
