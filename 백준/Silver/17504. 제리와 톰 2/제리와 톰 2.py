import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr = arr[::-1] # 리스트 뒤집기

numerator, denominator = 1, arr[0] # 분자, 분모

for i in range(1,n):
    numerator += arr[i]*denominator
    numerator, denominator = denominator, numerator
print(denominator - numerator, denominator)