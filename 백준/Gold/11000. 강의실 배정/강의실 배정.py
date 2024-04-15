import sys
import heapq
input = sys.stdin.readline

n = int(input())
classes = [list(map(int, input().split())) for _ in range(n)]

classes.sort(key = lambda x: (x[0], x[1]))# 시작, 끝나는 시간 기준으로 정렬
heap = [classes[0][1]] # 끝나는 시간 기록

for i in range(1, n):
    if classes[i][0] >= heap[0]: # 시작 시간이 전에 끝나는 시간보다 크다
        heapq.heappop(heap)
    heapq.heappush(heap, classes[i][1]) 

print(len(heap))

