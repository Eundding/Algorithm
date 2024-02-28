import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))

combi = list(combinations(arr, 3))
total = 0
for i in range(len(combi)):
    if sum(combi[i]) <= m:
        total = max(total, sum(combi[i]))
print(total)