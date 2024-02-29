import sys
input = sys.stdin.readline
n, k = map(int, input().split())
l = list(map(int, input().split()))
# 연속으로 k개의 최대 합

prefix = [0] # 누적합 리스트
temp = 0
for i in range(n):
    temp += l[i]
    prefix.append(temp)

answer = 0
for i in range(n):
    if i + k <= n:
        answer = max(answer, prefix[i+k]-prefix[i])
    else:
        answer = max(answer, prefix[n]-prefix[i]+prefix[(i+k)%n])

print(answer)
