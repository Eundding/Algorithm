import sys
input = sys.stdin.readline

n = int(input())
home = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n+1)]

# 초기값
dp[1][0] = home[0][0] #R
dp[1][1] = home[0][1] #G
dp[1][2] = home[0][2] #B

# dp[i][0] i번째까지 최솟값(R)
# dp[i][1] i번째까지 최솟값(G)
# dp[i][2] i번째까지 최솟값(B)
for i in range(2, n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + home[i-1][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + home[i-1][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + home[i-1][2]
print(min(dp[n][0], dp[n][1], dp[n][2]))