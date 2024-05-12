#include <iostream>
using namespace std;
int main() {
	int arr[10];
	int count[42] = { 0 };
	int NCount{ 0 };
	int a;
	for (int i = 0; i < 10; i++) {
		cin >> arr[i];
	}
	for (int j = 0; j < 10; j++) {
		a = arr[j] % 42;
		++count[a];
	}
	for (int k = 0; k < 42; k++) {
		if (count[k] != 0)
			NCount++;
	}
	cout << NCount;
}