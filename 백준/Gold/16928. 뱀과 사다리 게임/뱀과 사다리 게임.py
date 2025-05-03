import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue= deque()
    queue.append(1)

    while queue:
        x = queue.popleft()
        if x == 100:
            return graph[100]

        for i in range(1, 7):
            nx = x + i
            if nx < 1 or nx > 100: continue # 범위 밖
            if graph[nx] != 0: continue

            if nx in ladder.keys():
                nx = ladder[nx]
            elif nx in snake.keys():
                nx = snake[nx]
            if graph[nx] == 0:
                queue.append(nx)
                graph[nx] = graph[x]+1


n, m = map(int,input().split()) # n: 사다리, m: 뱀

# ladder, snake
snake = {}
ladder = {}
for i in range(n):
    a, b = map(int, input().split())
    ladder[a] = b
for i in range(m):
    a, b = map(int, input().split())
    snake[a] = b

graph = [0]*101
print(bfs())