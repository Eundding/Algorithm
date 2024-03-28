def solution(n):
    # n을 1, 2의 합으로 나타내는 경우의 수
    dp = [0]*2001
    dp[1], dp[2] = 1, 2
    
    for i in range(3, n+1):
        dp[i] = (dp[i-1]+dp[i-2])%1234567
    
    return dp[n]