import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    m = int(input())
    d = {}
    for i in range(m):
        a, b = input().split()
        if b in d.keys():
            d[b].append(a)
        else:
            d[b] = []
            d[b].append(a)

    if len(d) <= 1:
        print(m)
    else:
        cnt = 1
        for i in d.keys():
            cnt *= len(d[i])+1 # 안 입는 경우 때문에 +1
        print(cnt-1) # 모두 안 입은 경우 제외하기 위해 -1