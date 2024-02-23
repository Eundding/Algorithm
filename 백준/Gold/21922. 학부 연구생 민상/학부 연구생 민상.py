import sys
input = sys.stdin.readline


def wind_track(y, x, d):
    global cnt
    while True:
        y += dy[d]
        x += dx[d]
        if x < 0 or x >= m or y < 0 or y >= n:
            break
        if not visited[y][x]:
            visited[y][x] = True
            cnt += 1
        if laboratory[y][x] == 9:
            break

        elif laboratory[y][x] == 1:
            if d == 0 or d == 2:
                break
        elif laboratory[y][x] == 2:
            if d == 1 or d == 3:
                break
        elif laboratory[y][x] == 3:
            if d == 0:
                d = 3
            elif d == 1:
                d = 2
            elif d == 2:
                d = 1
            else:
                d = 0
        elif laboratory[y][x] == 4:
            if d == 0:
                d = 1
            elif d == 1:
                d = 0
            elif d == 2:
                d = 3
            else:
                d = 2
    return


n, m = map(int, input().split())  # n은 세로, m은 가로
laboratory = [list(map(int, input().split())) for i in range(n)]
visited = []
dx = [1, 0, -1, 0]  # 동; 남; 서; 북
dy = [0, 1, 0, -1]
cnt = 0
for i in range(n):
    visited.append([])
    for j in range(m):
        visited[-1].append(False)

for i in range(n):
    for j in range(m):
        if laboratory[i][j] == 9:
            if not visited[i][j]:
                visited[i][j] = True
                cnt += 1
            for k in range(4):
                wind_track(i, j, k)

print(cnt)
