from collections import deque

def bfs(x, n, computers):
    if visited[x]:
        return 0
    
    queue = deque([x])
    visited[x] = True
    
    while queue:
        node = queue.popleft()
        for i in range(n):
            if not visited[i] and computers[i][node]:
                visited[i] = True
                queue.append(i)
    
    return 1
    
    
        

def solution(n, computers):
    answer = 0
    global visited
    visited = [False]*n
    
    for i in range(n):
        answer += bfs(i, n, computers)

        
            
    
    return answer