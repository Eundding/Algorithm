#define _CRT_SECURE_NO_WARNINGS    // scanf 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>

int main()
{
	int n;
	int arr[31] = { 0, };
	for (int i = 1; i <= 28; i++) {
		scanf("%d", &n);
		arr[n] = 1;
	}


	for (int i = 1; i <= 30; i++) {
		if (arr[i] == 0) {
			printf("%d\n", i);
		}
	}

	return 0;
}