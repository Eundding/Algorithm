#define _CRT_SECURE_NO_WARNINGS    // scanf 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>

int main()
{
	int arr[11];
	int result = 0;

	for (int i = 0; i < 10; i++) {
		scanf("%d", &arr[i]);
		arr[i] %= 42;
	}

	for (int i = 0; i < 10; i++) {
		int flag = 1;
		for (int j = 0; j < i; j++) {
			if (arr[i] == arr[j]) {
				flag = 0; 
				break;
			}
		}
		if (flag == 1){
			result++;
		}
	}

	printf("%d", result);

	return 0;
}