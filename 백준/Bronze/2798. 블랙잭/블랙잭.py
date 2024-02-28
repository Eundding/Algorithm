# import sys
# input = sys.stdin.readline
# from itertools import combinations
#
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
#
# combi = list(combinations(arr, 3))
# total = 0
# for i in range(len(combi)):
#     if sum(combi[i]) <= m:
#         total = max(total, sum(combi[i]))
# print(total)

import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
combi = list(combinations(arr, 3))
sum_result = []
for i in range(len(combi)):
    sum_result.append( sum(combi[i]))
sum_result.sort()

answer = -1
sum_results = list(set(sum_result))

for i in range(len(sum_results)):
    if sum_results[i] <= m:
        answer = sum_results[i]

print(answer)