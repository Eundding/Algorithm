import sys
input = sys.stdin.readline
# 7795 먹을 것인가 먹힐 것인가
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    # A > B 개수
    idx = 0
    cnt = 0
    for i in range(n):
        while True:
            if idx == m or A[i] <= B[idx]:
                cnt += idx
                break
            else:
                idx += 1
    print(cnt)