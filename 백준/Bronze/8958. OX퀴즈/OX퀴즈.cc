#include <iostream>
#include <cstring>
using namespace std;
int main() {
	char arr[80];
	int n, i{ 0 }, count{ 0 }, score{ 0 }, size{ 0 };

	cin >> n;
	for (int k = 1; k <= n; k++) {
			cin >> arr; //O X 입력

		for (int j = 0; j < strlen(arr); j++) {
			if (arr[j] == 'O') {
				count += 1;
				score += count;
			}
			else count = 0;
		}
		cout << score << endl;
		score = 0;
		count = 0;
	}
	return 0;
}