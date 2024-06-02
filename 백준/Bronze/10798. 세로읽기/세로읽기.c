#define _CRT_SECURE_NO_WARNINGS    // scanf 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>

int main(void) {
    char arr[5][15] = {0};

    for (int i = 0; i < 5; i++) {
        scanf("%s", arr[i]);
    }
    for (int column = 0; column < 15; column++) {
        for (int row = 0; row < 5; row++) {
            if(arr[row][column] != NULL)
                printf("%c", arr[row][column]);
        }
    }

    return 0;
}