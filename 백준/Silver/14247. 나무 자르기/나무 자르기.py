import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
l2 = list(map(int, input().split()))
arr = [[0, 0] for _ in range(n)]
for i in range(n):
    arr[i][0], arr[i][1] = l[i], l2[i]

cnt = 0
arr.sort(key = lambda x: x[1])
for i in range(n):
    arr[i][0] += arr[i][1]*i
    cnt += arr[i][0]

print(cnt)