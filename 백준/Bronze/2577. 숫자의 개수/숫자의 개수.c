#define _crt_secure_no_warnings
#include <stdio.h>
#include <string.h>

int main() {
  int a, b, c;
  scanf("%d %d %d", &a, &b, &c);
  int result = a*b*c;
  char str[10];
  int arr[10] = {0};

  sprintf(str, "%d", result);
  for(int i = 0; i < strlen(str); i++){
    arr[str[i] - '0']++;
  }
  for(int i = 0; i < 10; i++){
    printf("%d\n", arr[i]);
  }
  
  return 0;
}