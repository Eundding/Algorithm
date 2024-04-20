#include <iostream>
using namespace std;
int main() {
	int x, y;
	cin >> x >> y;
	int a, b, c, d, e, f, g;
	a = x % 10;
	b = x / 10 % 10;
	c = x / 10 / 10;
	x = 100 * a + 10 * b + c;

	a = y % 10;
	b = y / 10 % 10;
	c = y / 10 / 10;
	y = 100 * a + 10 * b + c;

	if (x > y) cout << x;
	if (x < y) cout << y;
	
	return 0;
}