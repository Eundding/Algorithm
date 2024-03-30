#define _CRT_SECURE_NO_WARNINGS    // scanf 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>

int main() {
	int A;
	scanf("%d", &A);
	if ((A % 4 == 0 && A % 100 != 0) || (A % 400 == 0)) 
		printf("1");
	
	else 
		printf("0");
	


	return 0;
}