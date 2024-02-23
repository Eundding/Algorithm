import sys
from collections import deque
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(s, r, c):
    graph[r][c] = 'OK'
    queue = deque()
    queue.append((r, c))

    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nr = x + dr[i]
            nc = y + dc[i]

            if 0<=nr<n and 0<=nc<m:
                if graph[nr][nc] == s:
                    graph[nr][nc] = 'OK'
                    queue.append((nr, nc))
                    cnt += 1
    return cnt*cnt

m, n = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

W_value, B_value = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'W':
            W_value += bfs('W', i, j)

        if graph[i][j] == 'B':
            B_value += bfs('B', i, j)
print(W_value, B_value)