import sys
input = sys.stdin.readline

T = int(input())

dp = [1]*101
for i in range(4, 101):
    dp[i] = dp[i-2]+dp[i-3]

for _ in range(T):
    n = int(input())
    print(dp[n])