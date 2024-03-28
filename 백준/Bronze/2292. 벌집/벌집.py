import sys
input = sys.stdin.readline

N = int(input())

sum = 1
cnt = 1

while sum < N:
    sum += 6*cnt
    cnt += 1
print(cnt)
