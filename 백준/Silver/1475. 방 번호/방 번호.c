#define _crt_secure_no_warnings
#include <stdio.h>
#include <string.h>

int main() {
  char str[1000001];
  scanf("%s", str);
  int arr[10] = {0};

  for(int i = 0; i < strlen(str); i++){
    arr[str[i] - '0']++;
  }
  arr[6] = (arr[6] + arr[9] + 1 ) / 2;

  int max = 0;
  for(int i = 0; i < 9; i++){
    if(arr[i] > max) 
      max = arr[i];
  }
  printf("%d", max);
  
  
  return 0;
}