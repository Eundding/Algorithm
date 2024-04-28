#define _CRT_SECURE_NO_WARNINGS    // scanf 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>

int main()
{
	int n, m;
	scanf("%d %d", &n, &m);
	
	int arr[101] = { 0, };
	for (int i = 1; i <= n; i++) {
		arr[i] = i;
	}

	int a, b, temp;
	for (int i = 1; i <= m; i++) {
		scanf("%d %d", &a, &b);
		temp = arr[a];
		arr[a] = arr[b];
		arr[b] = temp;
	}

	for (int i = 1; i <= n; i++) {
		printf("%d ", arr[i]);
	}

	return 0;
}