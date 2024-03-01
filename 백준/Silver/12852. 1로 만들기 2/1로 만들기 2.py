import sys
input = sys.stdin.readline

n = int(input())

# dp 테이블 정의
# dp[k][1]
# dp[k][2]
# dp[k][3]

# 점화식
# dp[k][1] = max(dp[k-1][1], dp[k-1][2], dp[k-1][3]) + 1
# dp[k][2] = max(dp[k//2][1], dp[k//2][2], dp[k//2][3]) + 1
# dp[k][3] = max(dp[k//3][1], dp[k//3][2], dp[k//3][3]) + 1

# 초기값
# dp[1][1] = 1, dp[1][2] = 1, dp[1][3] = 1
# dp[2][1] =

dp = [0]*1000001
pre = [0]*1000001

dp[2], pre[2] = 1, 1
dp[3], pre[3] = 1, 1

if n == 1:
    print(0)
    print(1)
    exit()

elif n >= 4:
    for k in range(4, n+1):
        dp[k] = dp[k-1] + 1
        pre[k] = k-1

        if k % 3 == 0:
            if dp[k//3]+1 <= dp[k]:
                dp[k] = dp[k//3]+1
                pre[k] = k//3

        if k % 2 == 0:
            if dp[k//2]+1 <= dp[k]:
                dp[k] = dp[k//2]+1
                pre[k] = k//2

print(dp[n])
print(n, end=' ')
temp = n
while True:
    print(pre[temp], end=' ')
    temp = pre[temp]
    if temp == 1:
        break