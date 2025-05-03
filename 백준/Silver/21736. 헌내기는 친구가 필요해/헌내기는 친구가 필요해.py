import sys
from collections import deque
input = sys.stdin.readline

def findDY():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'I':
                return i, j

def bfs(x, y):
    cnt = 0
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue # 범위 밖
            if graph[nx][ny] == 'X': continue

            if not visited[nx][ny] and graph[nx][ny] == 'O':
                queue.append([nx, ny])
                visited[nx][ny] = 1
            if not visited[nx][ny] and graph[nx][ny] == 'P':
                cnt += 1
                queue.append([nx, ny])
                visited[nx][ny] = 1
    return cnt

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 도연 위치 찾기(I)
I_r, I_c = findDY()
visited[I_r][I_c] = 1
answer = bfs(I_r, I_c)

if answer == 0:
    print('TT')
else: print(answer)