import sys
input = sys.stdin.readline

n, s = map(int, input().split())
l = list(map(int, input().split()))
visited = [False]*n
global cnt
cnt = 0
def back(k, sum):
    global cnt
    if k == n:
        if sum == s:
            cnt += 1
        return

    back(k+1, sum+l[k])
    back(k+1, sum)

back(0, 0)
if s == 0: cnt -= 1
print(cnt)