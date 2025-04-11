import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque([(0, 0, 0)])
    while queue:
        x, y, z = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][z]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 범위 밖
                continue
            if graph[nx][ny] == 1 and z == 0: # 벽을 만났는데 아직 벽 안 부순 경우 => 벽 부수기
                # visited[nx][ny][z] = 1 # 방문
                visited[nx][ny][1] = visited[x][y][z] + 1
                queue.append((nx, ny, 1))
            elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0: # 벽X, 방문X
                # visited[nx][ny][z] = 1
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
    return -1


n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1 # (0,0) 방문 처리

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
print(bfs())