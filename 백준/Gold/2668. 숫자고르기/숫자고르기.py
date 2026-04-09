# 2668 숫자고르기
from collections import deque

def bfs(x):
    answer = []
    # 기준은 x
    visited = [False]*(n+1)
    queue = deque([x])
    visited[x] = True
    initial_value = x

    while queue:
        y = queue.popleft()
        answer.append(y)
            
        if not visited[num[y-1]]: 
            visited[num[y-1]] = True
            queue.append(num[y-1])
        elif num[y-1] == initial_value: # 한바퀴 돈것임
            return answer
    
    return False


n = int(input())
num = [int(input()) for _ in range(n)]

result = []
for i in range(1, n+1):
    if i == num[i-1]:
        result.append(i)
        continue

    answer = bfs(i)
    if answer: # 아무것도 없으면
        result.extend(answer)


result = set(result)
result = sorted(result)
print(len(result))
for i in result:
    print(i)