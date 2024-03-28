import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque()
for i in range(1, N+1):
    queue.append(str(i)) # 문자열 리스트로 해야 이따 join 이용 가능

answer = []
while queue:
    for _ in range(K-1):
        queue.append(queue.popleft()) # 맨 앞 원소 빼서 맨 뒤로 추가
    answer.append(queue.popleft())

print("<"+', '.join(answer)+">")