n, m = map(int, input().split())
ball = [0]*(n)
for _ in range(m):
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        ball[i-1] = c
print(*ball)