import sys
input = sys.stdin.readline

N, K, B = map(int, input().split())
broken = [False]*(N+1)

for i in range(B):
    broken[int(input())] = True

answer = []
for i in range(1, N+2-K):
    broken_cnt = 0
    traffic = 0
    for j in range(i, N+1):
        if broken[j]: # 고장난 상태
            broken_cnt += 1
        traffic += 1
        if traffic == K:
            break
    answer.append(broken_cnt)
print(min(answer))
