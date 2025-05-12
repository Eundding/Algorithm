import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c):
    queue = deque()
    queue.append([r, c])
    cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == '#':
                cnt += 1
                queue.append([nx, ny])
                graph[nx][ny] = 0
    return cnt


n, m, k = map(int, input().split())
graph = [[0]*m for _ in range(n)]
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
arr = []
for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = '#'
    arr.append([r-1, c-1])

result = []
for r, c in arr:
    result.append(bfs(r, c))
print(max(result))