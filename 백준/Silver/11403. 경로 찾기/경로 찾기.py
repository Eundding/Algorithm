from collections import deque

def bfs(x):
    queue = deque()
    queue.append(x)
    result = [0 for _ in range(n)]

    while queue:
        y = queue.popleft()
        for i in range(n):
            if result[i] == 0 and graph[y][i] == 1:
                queue.append(i)
                result[i] = 1
                visited[x][i] = 1

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

for i in range(0, n):
    bfs(i)

for i in visited:
    print(*i)