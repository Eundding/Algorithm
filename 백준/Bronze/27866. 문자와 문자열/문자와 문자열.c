#define _CRT_SECURE_NO_WARNINGS    // scanf 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>

int main()
{
	char arr[1001];
	int i;
	scanf("%s", arr);
	scanf("%d", &i);
	printf("%c", arr[i - 1]);

	return 0;
}