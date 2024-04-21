import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# dp[n] => n까지 최대로 넣을 수 있는 상자 개수
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))