#include <iostream>
using namespace std;
int arr[1000001];
void prime(int x, int y) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	for (int i = 2; i <= y; i++) {
		arr[i] = i;
	}
	for (int i = 2; i <= y; i++) {
		if (arr[i] == 0) continue;
		for (int j = i + i; j <= y; j += i) {
			arr[j] = 0;
		}
	}
	for (int k = x; k <= y; k++) {
		if (arr[k] != 0)
			cout << k << '\n';
	}
}
int main() {
	int m, n;
	cin >> m >> n;
	prime(m, n);
}