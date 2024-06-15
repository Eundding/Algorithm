#define _crt_secure_no_warnings
#include <stdio.h>
#include <string.h>

int MAX = 100;

int main() {
  int arr[26] = { 0 };
  char str[MAX];

  scanf("%s", str);

  for (int i = 0; i < strlen(str); i++) {
    arr[str[i] - 'a']++;
  }

  for (int j = 0; j < 26; j++) {
    printf("%d ", arr[j]);
  }

  return 0;
}