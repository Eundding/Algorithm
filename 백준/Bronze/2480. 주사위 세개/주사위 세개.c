#define _CRT_SECURE_NO_WARNINGS    // scanf 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>

int main() {
	int A, B, C;
	scanf("%d %d %d", &A, &B, &C);

	if (A == B && B == C)
		printf("%d", 10000+ A * 1000);
	else if(A == B && B != C)
		printf("%d", 1000 + B * 100);
	else if (C == B && B != A)
		printf("%d", 1000 + B * 100);
	else if (A == C && B != A)
		printf("%d", 1000 + A * 100);
	else
		if (A>B && A>C)
			printf("%d", A*100);
		else if (A < B && B > C)
			printf("%d", B * 100);
		else
			printf("%d", C * 100);

	 
	return 0;
}