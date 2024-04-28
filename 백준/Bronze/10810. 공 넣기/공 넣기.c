#define _CRT_SECURE_NO_WARNINGS    // scanf 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>

int main()
{
	int n, m;

	scanf("%d %d", &n, &m);
	
	int arr[101] = { 0, };
	int a, b, c;
	for (int i = 1; i <= m; i++) {
		
		scanf("%d %d %d", &a, &b, &c);

		for (int j = a; j <= b; j++) {
			arr[j] = c;
		}
	}

	for (int i = 1; i <= n; i++) {
		printf("%d ", arr[i]);
	}

	return 0;
}