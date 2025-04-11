import sys
import heapq
input = sys.stdin.readline
"""
최소힙
절댓값이 가장 작은 값 출력
절댓값이 가장 작은 값이 여러개라면 가장 작은 수 출력
"""
n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if not heap:
            print(0)
        else:
            y = heapq.heappop(heap)
            if y[1] == False:
                print(-y[0])
            else:
                print(y[0])
        continue

    if x > 0:
        temp = True
    else:
        temp = False
        x = -x

    heapq.heappush(heap,(x,temp)) # 부호와 같이 저장