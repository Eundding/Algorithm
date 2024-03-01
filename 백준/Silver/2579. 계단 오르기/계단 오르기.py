import sys
input = sys.stdin.readline
n = int(input())
stairs = [int(input()) for _ in range(n)]

# 1. 테이블 정의
# dp[i][j] = 현재까지 j개의 계단을 연속해서 밟고 i번째 계단까지 올라섰을 때 점수 합의 최댓값,
# 단 i 번째 계단은 반드시 밟아야 함

# 2. 점화식 찾기
# dp[k][1] = max(dp[k-2][2], dp[k-2][1]) + stairs[k]
# dp[k][2] = dp[k-1][1] + stairs[k]

# 3. 초기값
# dp[1][1] = stairs[1]
# dp[1][2] = 0
# dp[2][1] = stairs[2]
# dp[2][2] = stairs[1] + stairs[2]

if n == 1:
    print(stairs[0])
else:
    dp = [[0]*3 for _ in range(n+1)]
    dp[1][1] = stairs[0]
    dp[1][2] = 0
    dp[2][1] = stairs[1]
    dp[2][2] = stairs[0] + stairs[1]
    for i in range(3, n+1):
        dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + stairs[i-1]
        dp[i][2] = dp[i-1][1] + stairs[i-1]
    print(max(dp[n][1], dp[n][2]))
