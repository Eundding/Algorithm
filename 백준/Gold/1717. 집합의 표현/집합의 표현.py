import sys
sys.setrecursionlimit(1000000) # 재귀 깊이 제한 늘리기
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int, input().split())
parent = list(range(n+1))

for _ in range(m):
    s, a, b = map(int, input().split())
    if s == 0:
        union(a, b)
    else: # s==1
        # if parent[a] == parent[b]:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')