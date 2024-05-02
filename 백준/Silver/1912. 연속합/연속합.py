import sys
input = sys.stdin.readline
'''
dp[n] = > 인덱스 n까지 숫자 합 중 최댓값
'''
n = int(input())
arr = list(map(int, input().split()))

for i in range(1, n):
    arr[i] = max(arr[i], arr[i]+arr[i-1])

print(max(arr))