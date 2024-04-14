#define _CRT_SECURE_NO_WARNINGS    // scanf 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n -i; j++) {
			printf(" ");
		}
		for (int k = 1; k <= i; k++) {
			printf("*");
		}
		printf("\n");
	}
	
	return 0;
}