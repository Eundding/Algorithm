#define _CRT_SECURE_NO_WARNINGS    // scanf 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>

int main()
{
	int n;
	scanf("%d", &n);

	int x;
	scanf("%d", &x);

	int arr[10001];
	for (int i = 0; i < n; i++) {
		scanf("%d", &arr[i]);
	}
	

	for (int i = 0; i < n; i++) {
		if (arr[i] < x) {
			printf("%d ", arr[i]);
		}
	}

}

