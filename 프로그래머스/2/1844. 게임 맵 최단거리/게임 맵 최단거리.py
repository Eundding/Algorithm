from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(maps, n, m):
    graph = [[-1]*m for _ in range(n)]
    graph[0][0] = 1
    queue = deque()
    queue.append([0, 0])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
                   
            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 범위 밖
                continue
                
            if maps[nx][ny] == 1 and (graph[nx][ny] == -1 or graph[nx][ny] > graph[x][y]+1): 
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])
            elif nx == n-1 and ny == m-1: # 도착 지점
                graph[nx][ny] = min(graph[x][y] + 1, graph[nx][ny])
        
    return graph[n-1][m-1]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = bfs(maps, n, m)
    return answer
    
#     if graph[n-1][m-1] == -1:
#         return -1
#     else:
#         return graph[n-1][m-1]
