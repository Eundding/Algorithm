#define _CRT_SECURE_NO_WARNINGS    // scanf 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>

int main()
{
	int n;
	scanf("%d", &n);

	int arr[1000001];
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}


	int max = arr[0];
	int min = arr[0];
	for (int i = 1; i < n; i++) {
		if (arr[i] > max) {
			max = arr[i];
		}

		if (arr[i] < min) {
			min = arr[i];
		}
	}
	printf("%d %d", min, max);
}

