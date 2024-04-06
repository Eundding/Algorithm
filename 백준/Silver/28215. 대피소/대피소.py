import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())
x = [0]*n
y = [0]*n
for i in range(n):
    x[i], y[i] = map(int, input().split())

INF = float("INF")

def dist(c):
    b = 0
    for i in range(n):
        a = INF
        for j in c:
            temp = abs(x[i] - x[j]) + abs(y[i] - y[j])
            a = min(a, temp)
        b = max(b, a)
    return b
comb = list(combinations(range(n), k))
answer = INF
for c in comb:
    answer = min(answer, dist(c))

print(answer)
