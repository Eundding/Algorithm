//행렬 곱셈
#include <iostream>
using namespace std;
int arr3[100][100];
int main() {
	int n{ 0 }, m, m1, k, x{ 0 };
	int arr1[100][100], arr2[100][100];

	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> arr1[i][j];
		}
	}

	cin >> m1 >> k;
	for (int a = 0; a < m1; a++) {
		for (int b = 0; b < k; b++) {
			cin >> arr2[a][b];
		}
	}

	int c{ 0 }, d{ 0 }, e{ 0 };
	while (true) {
		for (int c = 0; c < n; c++) {
			for (int d = 0; d < k; d++) {
				for (int e = 0; e < m; e++) {
					arr3[c][d] += arr1[c][e] * arr2[x][d];
					if (x > m - 1) break;
					x++;
				}
				x = 0;
			}
			e == 0, x == 0;
			if (c == n - 1) break;
		}
		break;
	}
	
	for (int f = 0; f < n; f++) {
		for (int g = 0; g < k; g++) {
			cout << arr3[f][g] << " ";
		}
		cout << endl;
	}
}

