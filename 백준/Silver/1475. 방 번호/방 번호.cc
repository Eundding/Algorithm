#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	string n;
	cin >> n;

	int cnt = 0;
	int arr[10] = {};
	int num;

	for (int i = 0; i < n.length(); i++) {
		num = n[i]- '0';
		arr[num]++;
	}

	arr[9] += arr[6]; arr[6] = 0;
	int max = arr[0];

	for (int j = 1; j < 9; j++) {
		if (arr[j] > max) max = arr[j];
	}

	if (arr[9] / 2 >= max) {
		if (arr[9] % 2 == 1) max = arr[9] / 2 + 1; //홀수면
		else max = arr[9] / 2;
	}
	
	cout << max;

	return 0;
}